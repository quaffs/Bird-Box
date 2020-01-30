var express = require('express');
var router = express.Router();

/* GET classify listing. */
router.get('/', function (req, res, next) {
  res.send('respond with a resource');
});

/* GET example process. 
   This demonstrates how a python process can be started from node*/
router.get('/exampleProcess', function (req, res, next) {
  var spawn = require("child_process").spawn;
  // runs a process.  Including arguments
  var process = spawn('python3', ["./HelloWorld.py", "Test Param"]);
  // send data from output of spawned process to route
  process.stdout.on('data', function (data) {
    res.send(data.toString());
  });
});

/* POST upload sound. 
   This demonstrates how a the upload sound route can be reached */
router.post('/uploadSound', function (req, res, next) {
  console.log("Upload Sound Route Reached");
  res.send("Hello World");
});

/* POST response example. 
   This demonstrates how a the upload sound route can be reached */
router.post('/responseExample', function (req, res, next) {
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

module.exports = router;