var fs = require('fs');
var path =  require('path');
var _ = require('lodash');
var LOG = 0;

function f1() {
  var dirpath = './../data/tidigit/train/man';
  var SCP_File = './../io/created/scp/man.scp'
  createSCP(dirpath, SCP_File);
  console.log('CREATING man.SCP')
}

function f2() {
  var dirpath = './../data/tidigit/train/woman';
  var SCP_File = './../io/created/scp/woman.scp'
  createSCP(dirpath, SCP_File);
  console.log('CREATING woman.SCP')
}
// *** put the above f1, f2 .. in funs array to execute one by one
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
function createSCP(dirpath, SCP_File) {
  
  var data = []; // *** all string will be pushed to this array ***

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
            processFiles(files, dpath, data, SCP_File);
          })
        } else {
          count--;
        }
      }) // fs.stat

    }) // dirs.forEach
  })
}

var inc = 0;

function processFiles(files, dpath, data, SCP_File) {
  files.forEach( function (fname){
    var filePath = path.join(dpath, fname);

    if (LOG) console.log(++inc,' ->', filePath);
    putFileInfo(filePath, fname, data);
  
    // ***create the SCP file***
    if(--count == 0) {
      // save file
      console.log('SAVING THE SCP FILE.');

      // console.log(data.join(''))
      // fs.writeFile(SCP_File, data.join(''), function (err) {
      //   if(err) console.log(err)

        runNextFun();
        inc = 0;
      // })

    }
  })
}

var absFilePath = '';
function putFileInfo(filePath, fname, data) {
  // the mfcc absolute file path
  absFilePath = path.resolve(__dirname, filePath);

  // the mfcc absolute file path
  var savePath = path.resolve(__dirname, '../io/gen/scp');
  savePath += fname;

  var str = absFilePath +'        '+ savePath + '\n';
  console.log(str)
  data.push(str);
}