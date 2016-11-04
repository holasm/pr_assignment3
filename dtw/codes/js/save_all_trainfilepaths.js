var fs = require('fs');
var path = require('path');
var _ = require('underscore')

// var testSaveRoot = '../../data/processed/test/'
var trainRoot = '../../data/processed/train/'
var trainSaveFile = '../../data/processed/train.txt'

var dirs = fs.readdirSync(trainRoot);

var trainPaths = [];
dirs.forEach((dir, index)=>{
  if(dir != '.DS_Store'){ 
    var dPath = path.resolve(trainRoot, dir);
    var filesList = fs.readdirSync(dPath);
    
    filesList.forEach((file, index)=>{
      var fPath = path.resolve(dPath, file);
      trainPaths.push(fPath);
    })
  }
})

// create a new train file which will contain all files path
fs.writeFileSync(trainSaveFile, trainPaths.join('\n'));
console.log('-*------')
