var fs = require('fs');
var path =  require('path');
var _ = require('lodash');
var LOG = 0;

/*
 * 1. Copies mfcc files after removing first line
 * 2. cteates .mlf file
 * 3. creates .scp file
 */

function f1() {
  var dirpath = './../data/tidigit/test/man';
  var MLF_File = './../io/created/test/mlf/man.mlf';
  createMLF(dirpath, MLF_File);
  console.log('CREATING man.mlf')
}

function f2() {
  var dirpath = './../data/tidigit/test/woman';
  var MLF_File = './../io/created/test/mlf/woman.mlf';
  createMLF(dirpath, MLF_File);
  console.log('CREATING woman.mlf')
}

var funs = [f1, f2];
var first = 1;
runNextFun();

// 
function runNextFun() {
  if(first){
    first = 0;
    funs[0] && funs[0]();
  } else {
    funs.shift();
    funs[0] && funs[0]();
  }
}

var count; // keep track of remaining files
function createMLF(dirpath, MLF_File) {
  var data = ['#!MLF!#\n'];
  fs.readdir(dirpath, function (err, dirs) {
    count = dirs.length;
    if (err) console.log(err);
    dirs.forEach(function (dir, index) { // dir -> ae, mn, ns ...
      // dir is directory with featuer files
      var dpath = path.join(dirpath, dir); // create path for dir...
      fs.stat(dpath, function (err, stats) {
        // console.log(dpath)
        if(stats.isDirectory()){
          fs.readdir(dpath, function (err, files) {
            count--;
            count += files.length;

            if (err) console.log(err);
            processFiles(files, dpath, data, MLF_File);
          })
        } else {
          count--;
        }
      }) // fs.stat

    }) // dirs.forEach
  })
}

var inc = 0;
function processFiles(files, dpath, data, MLF_File) {
  files.forEach( function (fname){
    var filePath = path.join(dpath, fname);
    // ***create the MLF file***
    // console.log(filePath)
    if (LOG) console.log(++inc,' ->', filePath);
    putFileInfo(filePath, fname, data);
  
    if(--count == 0) {
      // save file
      console.log('SAVING THE MLF FILE.');

      // console.log(data.join(''))
      // fs.writeFile(MLF_File, data.join(''), function (err) {
      //   if(err) console.log(err)

        runNextFun();
        inc = 0;
      // });

    }
  })
}
var key = 1;
function putFileInfo(filePath, fname, data) {
  fs.readFile(filePath, 'utf-8', function (err, data) {
    if (err) new Error(err);
    // remove first line from data
    // write the file
    var newLine = data.indexOf('\n');
    var processedFilePath = filePath.replace('tidigit', 'processed');
    if (!fs.existsSync(processedFilePath.slice(0, -fname.length))){
      fs.mkdirSync(processedFilePath.slice(0, -fname.length));
    }
    
    RE = /([0-9])/gi;

    if(fname.search(RE) >= 0){
      // console.log(processedFilePath)
      fs.writeFile(processedFilePath, data.slice(newLine+1));
    }
  })
}