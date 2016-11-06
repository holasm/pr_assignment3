var fs = require('fs');
var path =require('path');
var _ = require('underscore');

var paths = './../../data/processed/paths/';
var testPathsDir = './../../data/processed/testPaths/';
var trainPathsDir = './../../data/processed/trainPaths/';

var fData = fs.readdirSync(paths);
fData.forEach((file, index)=>{
  var testPaths = "";
  var trainPaths = "";
  fPath = path.resolve(paths, file);
  data = fs.readFileSync(fPath);
  data = JSON.parse(data)
  var kuchvi = _.shuffle(_.range(data.length));
  var divider = Math.floor(kuchvi.length * 0.25);
  for (var i = 0; i < divider; i++) {
    testPaths += path.resolve(__dirname,data[kuchvi[i]]) + "\n";
  }
  testPaths = testPaths.slice(0, -1);
  for (var i = divider; i < data.length; i++) {
    trainPaths += path.resolve(__dirname, data[kuchvi[i]]) + "\n";
  }
  trainPaths = trainPaths.slice(0, -1);
  fbase = file.slice(0, -5)
  fs.writeFileSync(testPathsDir+fbase+'.txt', testPaths)
  fs.writeFileSync(trainPathsDir+fbase+'.txt', trainPaths)
  // console.log(testPaths.split('\n').length, trainPaths.split('\n').length, data.length)
})