var express = require("express");
var router = express.Router();
var fs = require("fs");
var shortid = require("shortid");
var child = require("child_process");
var multer = require("multer");
var upload = multer({ dest: "tmp/" });
var path = require("path");

var audioInputDir = "./public/audio/";

/* GET classify listing. */
router.get("/", function(req, res, next) {
  res.send("respond with a resource");
});

/* GET example process. 
   This demonstrates how a python process can be started from node*/
router.get("/exampleProcess", function(req, res, next) {
  var spawn = require("child_process").spawn;
  // runs a process.  Including arguments
  var process = spawn("python3", ["./HelloWorld.py", "Test Param"]);
  // send data from output of spawned process to route
  process.stdout.on("data", function(data) {
    res.send(data.toString());
  });
});

/* Post upload form */
var fileUpload = upload.fields([
  { name: "file1" },
  { name: "file2" },
  { name: "file3" }
]);
router.post("/uploadForm", fileUpload, function(req, res, next) {
  // create ID for process and create directory
  var id = shortid.generate();
  var result = { id: id };
  var curAudioDir = audioInputDir + id;
  console.log(`Upload Form Route Reached (id: ${id})`);
  if (!fs.existsSync(curAudioDir)) fs.mkdirSync(curAudioDir);
  // process files
  var processResult = processFiles(req.files, curAudioDir);
  Object.assign(result, processResult);
  res.json(result);
});

/* POST upload sound. 
   This demonstrates how a the upload sound route can be reached */
router.post("/uploadSound", function(req, res, next) {
  var id = shortid.generate(); // id for process
  console.log(`Upload Sound Route Reached (id: ${id})`);
  // audio file should be saved locally
  var curAudioDir = audioInputDir + id;
  if (!fs.existsSync(curAudioDir)) fs.mkdirSync(curAudioDir);
  fileName = "CardinalCallTest.wav";
  // create process to segment audio into 10 second segments
  var processData, processError;
  var process = spawn("ffmpeg", [
    "-i",
    audioInputDir + fileName,
    "-f",
    "segment",
    "-segment_time",
    "10",
    "-c",
    "copy",
    curAudioDir + "out%03d.wav"
  ]);
  process.stdout.on("data", function(data) {
    processData = data.toString();
  });
  process.stderr.on("data", function(error) {
    processError = error.toString();
  });
  process.stdout.on("end", function() {
    res.json({
      data: processData,
      error: processError
    });
  });
});

/* POST response example. 
   This demonstrates how a the upload sound route can be reached */
router.post("/responseExample", function(req, res, next) {
  console.log("Name:", req.body.name);
  console.log("Message:", req.body.message);
  exampleJSON = {};
  exampleJSON.fileName = "testFile.wav";
  exampleJSON.success = true;
  exampleJSON.results = {
    0: {
      classification: "cardinal",
      timeStart: 5,
      timeEnd: 10
    },
    1: {
      classification: "blue jay",
      timeStart: 13,
      timeEnd: 20
    },
    2: {
      classification: "cardinal",
      timeStart: 31,
      timeEnd: 37
    }
  };
  res.json(exampleJSON);
});

function processFiles(files, audioDir) {
  response = { msg: "", error: "" };
  for (const key in files) {
    file = files[key][0];
    // move file to directory
    var newPath = path.join(audioDir, key);
    fs.renameSync(file.path, `${newPath}.wav`);
    // segment file
    segmentDir = `${newPath}Segs`;
    return segmentFiles(`${newPath}.wav`, segmentDir, 10);
  }
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

module.exports = router;
