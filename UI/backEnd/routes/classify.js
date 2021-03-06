var express = require("express");
var router = express.Router();
var fs = require("fs");
var shortid = require("shortid");
var child = require("child_process");
var multer = require("multer");
var upload = multer({ dest: "tmp/" });
var path = require("path");

var audioInputDir = "./public/audio/";

/* Post upload form */
var fileUpload = upload.fields([
  { name: "file1" },
  { name: "file2" },
  { name: "file3" },
  { name: "file4" },
  { name: "file5" }
]);
router.post("/uploadForm", fileUpload, function(req, res, next) {
  // create ID for process and create directory
  var id = shortid.generate();
  var results = { id: id, classifyResults: [] };
  var curAudioDir = audioInputDir + id;
  console.log(`Upload Form Route Reached (id: ${id})`);
  if (!fs.existsSync(curAudioDir)) fs.mkdirSync(curAudioDir);
  // process files
  var processResult = processFiles(req.files, curAudioDir);
  // make sure all results were process, then run algorithms
  if (!processResult.error) {
    for (var i = 0; i < processResult.fileCount; i++) {
      // run classify script for all files at same time
      var classifications = [];
      for (var j = 0; j < processResult.segResults.length; j++) {
        // send to classification algorithm
        classifications.push(
          classify(
            path.join(
              curAudioDir,
              `file${j + 1}Segs`,
              `seg${i.toString().padStart(3, "0")}.wav`
            )
          )
        );
      }
      // send to direction and distance algorithm

      classifySingleResult = distanceAndDirection(classifications, i);
      if (classifySingleResult.direction != "") {
        results.classifyResults.push(classifySingleResult);
      }
    }
  }
  // run direction/distance algorithm
  Object.assign(results, processResult);
  res.json(results);
});

function processFiles(files, audioDir) {
  var response = { segResults: [], error: false, errorMsg: "", fileCount: 0 };
  var fileCounts = [];
  for (const key in files) {
    file = files[key][0];
    // move file to directory
    var newPath = path.join(audioDir, key);
    fs.renameSync(file.path, `${newPath}.wav`);
    // segment file
    segmentDir = `${newPath}Segs`;
    response.segResults.push(segmentFiles(`${newPath}.wav`, segmentDir, 10));
    fileCounts.push(fs.readdirSync(path.join(audioDir, `${key}Segs`)).length);
  }
  // make sure files process correctly
  if (!resultsProcessedCorrect(response.segResults)) {
    response.error = true;
    response.errorMsg = "Files were not properly processed";
    return response;
  }
  // make sure file count is correct
  if (!fileCounts.every((val, i, arr) => val === arr[0])) {
    response.error = true;
    response.errorMsg = "Files did not have same length";
    return response;
  }
  response.fileCount = fileCounts[0];
  return response;
}

function segmentFiles(filePath, outputDir, length) {
  // make sure file exists
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
  }
  // run segment process by calling ffmpeg system process
  var process = child.spawnSync("ffmpeg", [
    "-i",
    filePath,
    "-f",
    "segment",
    "-segment_time",
    length,
    "-c",
    "copy",
    path.join(segmentDir, "seg%03d.wav")
  ]);
  return {
    success: process.status === 0 ? true : false,
    processError: process.stderr.toString()
  };
}

function resultsProcessedCorrect(segResults) {
  result = true;
  segResults.forEach(r => {
    if (!r.success) result = false;
  });
  return result;
}

function classify(filePath) {
  console.log(filePath);
  var result = { callDetected: -1, classification: "null" };
  var process = child.spawnSync("python3", ["./classify.py", filePath]);
  if (process.status === 0) {
    var lines = process.stdout.toString().split("\n");
    result.callDetected = parseInt(lines[0]);
    result.classification = lines[1];
  }
  else {
    console.log(result.stderr.toString());
  }
  return result;
}

function distanceAndDirection(classifications, i) {
  console.log(classifications);
  var result = {
    classification: "",
    distance: 0,
    direction: "",
    timeStart: 0,
    timeEnd: 0
  };
  var classificationArray = [];
  classifications.forEach(e => {
    if (e.classification != "Non-Cardinal")
      result.classification = e.classification;
    classificationArray.push(e.callDetected);
  });
  classificationArraySum = classificationArray.reduce((a, b) => a + b, 0);
  if (classificationArraySum > 0) {
    var process = child.spawnSync("python3", [
      "./distanceAndDirection.py",
      classificationArray.join(" ")
    ]);
    if (process.status === 0) {
      var lines = process.stdout.toString().split("\n");
      result.distance = lines[0];
      result.direction = lines[1];
      result.timeStart = i * 10;
      result.timeEnd = i * 10 + 10;
    }  else {
      console.log(result.stderr.toString());
    }
  }
  return result;
}

module.exports = router;
