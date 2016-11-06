var fs = require('fs');
var path = require('path');

var testPaths = "./../../data/processed/testPaths/";
var trainPaths = "./../../data/processed/trainPaths/";
var testMlfPaths = "./../../io/created/mlf/test/";
var trainMlfPaths = "./../../io/created/mlf/train/";
var testMlfDatAll = '';
var trainMlfDatAll = '';

var testFiles = fs.readdirSync(testPaths);
testFiles.forEach((file)=>{
  var mlfData = "";

  var fPath = path.resolve(testPaths, file);
  var data = fs.readFileSync(fPath, 'utf-8'); // read file from absolute path
  data = data.split('\n');
  data.forEach((mfccPath)=>{
    var fName = path.basename(mfccPath)
    mlfData += '\"*/';
    mlfData += fName.slice(0,-5)+'.lab';// filename.lab
    mlfData += '\"\n';
    mlfData += file.slice(0, -4)
    mlfData += '\n.\n';
  })
  mlfData = mlfData.slice(0, -1);
  // console.log(mlfData);

  // write to mlf file
  var mlfPath = testMlfPaths+file.slice(0, -4)+'.mlf'
  fs.writeFileSync(mlfPath, "#!MLF!#\n" + mlfData);
  testMlfDatAll += mlfData + '\n';
})
fs.writeFileSync(testMlfPaths+'../test.mlf', "#!MLF!#\n"+testMlfDatAll);

var trainFiles = fs.readdirSync(trainPaths);
trainFiles.forEach((file)=>{
  var mlfData = "";

  var fPath = path.resolve(trainPaths, file);
  var data = fs.readFileSync(fPath, 'utf-8'); // read file from absolute path
  data = data.split('\n');
  data.forEach((mfccPath)=>{
    var fName = path.basename(mfccPath)
    mlfData += '\"*/';
    mlfData += fName.slice(0,-5)+'.lab';// filename.lab
    mlfData += '\"\n';
    mlfData += file.slice(0, -4)
    mlfData += '\n.\n';
  })
  mlfData = mlfData.slice(0, -1);
  // console.log(mlfData);

  // write to mlf file
  var mlfPath = trainMlfPaths+file.slice(0, -4)+'.mlf'
  fs.writeFileSync(mlfPath, "#!MLF!#\n" + mlfData);
  trainMlfDatAll += mlfData + '\n';
})
fs.writeFileSync(trainMlfPaths+'../train.mlf', "#!MLF!#\n"+trainMlfDatAll);