var express = require('express');
var router = express.Router();

/* GET classify listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

/* GET example process. 
   This demonstrates how a python process can be started from node*/
router.get('/exampleProcess', function(req, res, next) {
  var spawn = require("child_process").spawn;
  // runs a process.  Including arguments
  var process = spawn('python3',["./HelloWorld.py", "Test Param"]);
  // send data from output of spawned process to route
  process.stdout.on('data', function(data) {
    res.send(data.toString());
  });
});

/* GET example process. 
   This demonstrates how a the upload sound route can be reached */
   router.post('/uploadSound', function(req, res, next) {
     console.log("Upload Sound Route Reached");
    res.send("Hello World");
  });

module.exports = router;
