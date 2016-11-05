var fs = require('fs');
var path = require('path');
var _ = require('underscore')

// var testSaveRoot = '../../data/processed/test/'
var testRoot = '../../data/processed/test/'
var testSaveFile = '../../data/processed/test.txt'

var dirs = fs.readdirSync(testRoot);

var testPaths = [];
dirs.forEach((dir, index)=>{
  if(dir != '.DS_Store'){ 
    var dPath = path.resolve(testRoot, dir);
    var filesList = fs.readdirSync(dPath);
    
    filesList.forEach((file, index)=>{
      var fPath = path.resolve(dPath, file);
      testPaths.push(fPath);
    })
  }
})

// create a new test file which will contain all files path
fs.writeFileSync(testSaveFile, testPaths.join('\n'));
console.log('-*------')
