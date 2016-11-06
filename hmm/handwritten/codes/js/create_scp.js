var fs = require('fs');
var path = require('path');

var testPaths = "./../../data/processed/testPaths/";
var trainPaths = "./../../data/processed/trainPaths/";
var testScpPaths = "./../../io/created/scp/test/";
var trainScpPaths = "./../../io/created/scp/train/";
var testScpDatAll = '';
var trainScpDatAll = '';

var testFiles = fs.readdirSync(testPaths);
testFiles.forEach((file)=>{
  var fPath = path.resolve(testPaths, file);
  var data = fs.readFileSync(fPath, 'utf-8'); // read file from absolute path
  data = data.split('\n');
  data.forEach(function(part, index, theArray) {
    theArray[index] = part.slice(0, -5) + '.htk';
  });
  data = data.join('\n');
  // console.log(data)
  // write to scp file
  var scpPath = testScpPaths+file.slice(0, -4)+'.scp'
  fs.writeFileSync(scpPath, data);
  testScpDatAll += data + '\n';
})

fs.writeFileSync(testScpPaths+'../test.scp', testScpDatAll);

var trainFiles = fs.readdirSync(trainPaths);
trainFiles.forEach((file)=>{
  var fPath = path.resolve(trainPaths, file);
  var data = fs.readFileSync(fPath, 'utf-8'); // read file from absolute path
  data = data.split('\n');
  data.forEach(function(part, index, theArray) {
    theArray[index] = part.slice(0, -5) + '.htk';
  });
  data = data.join('\n');
  // console.log(data)
  // write to scp file
  var scpPath = trainScpPaths+file.slice(0, -4)+'.scp'
  fs.writeFileSync(scpPath, data);
  trainScpDatAll += data + '\n';
})

fs.writeFileSync(testScpPaths+'../train.scp', testScpDatAll);


