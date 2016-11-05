var fs = require('fs');
var path = require('path');
var _ = require('underscore');

var rootPath = './../../data/test-1/';
var testPath = './../../data/test.json'

var count = 0;
var data = []
var files = fs.readdirSync(rootPath)
files.forEach( function (dpath, index) {
  var filesPath =  rootPath + dpath;
  var stats = fs.statSync(filesPath)
  if(stats.isDirectory()) {
    var mfccFiles = fs.readdirSync(filesPath);
    for (var i = mfccFiles.length - 1; i >= 0; i--) {
      var fPath = filesPath + '/' + mfccFiles[i];
      fPath = path.resolve(__dirname, fPath);
      data.push(fPath);
    }
  }
})

fs.writeFileSync(testPath, JSON.stringify(data));
// console.log(JSON.stringify(data))
