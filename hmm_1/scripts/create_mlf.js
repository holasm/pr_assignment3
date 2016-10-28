var fs = require('fs');
var path =  require('path');
var _ = require('lodash');

var dirpath = './../data/tidigit/train/man';
var manMLF_File = './../man.mlf'
createMLF(dirpath);

var count;

function createMLF(dirpath) {
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
            processFiles(files, dpath);
          })
        } else {
          count--;
        }
      }) // fs.stat

    }) // dirs.forEach
  })
}

var inc = 0;
var data = [];
function processFiles(files, dpath) {
  files.forEach( function (fname){
    var filePath = path.join(dpath, fname);
    // ***create the MLF file***
    console.log(++inc,' ->', filePath);
    putFileInfo(filePath, fname);
  
    if(--count == 0) {
      // save file
      console.log('SAVING THE MLF FILE.');

      console.log(data.join(''))
      fs.writeFile(manMLF_File, data.join(''), function (err) {
        if(err) console.log(err)
      })

    }
  })
}

function putFileInfo(filePath, fname) {
  var str = '"*/' + fname + '"\n';
  var name = fname.slice(0, -5);
  for (var i = 0; i < name.length; i++) {
    str += name[i] + '\n';
  }

  str += '.\n';

  console.log(str)

  data.push(str);
}