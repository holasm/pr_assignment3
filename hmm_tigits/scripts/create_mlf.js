var fs = require('fs');
var path =  require('path');
var _ = require('lodash');
var LOG = 0;

function f1() {
  var dirpath = './../data/tidigit/train/man';
  var MLF_File = './../io/created/mlf/man.mlf'
  createMLF(dirpath, MLF_File);
  console.log('CREATING man.mlf')
}

function f2() {
  var dirpath = './../data/tidigit/train/woman';
  var MLF_File = './../io/created/mlf/woman.mlf'
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
      fs.writeFile(MLF_File, data.join(''), function (err) {
        if(err) console.log(err)

        runNextFun();
        inc = 0;
      })

    }
  })
}

var names = {
  // 'a' : 'a',
  // 'b' : 'b',
  // 'c' : 'c',
  // 'd' : 'd',
  // 'e' : 'e',
  // 'f' : 'f',
  // 'g' : 'g',
  // 'h' : 'h',
  // 'i' : 'i',
  // 'j' : 'j',
  // 'k' : 'k',
  // 'l' : 'l',
  // 'm' : 'm',
  // 'n' : 'n',
  // 'o' : 'o',
  // 'p' : 'p',
  // 'q' : 'q',
  // 'r' : 'r',
  // 's' : 's',
  // 't' : 't',
  // 'u' : 'u',
  // 'v' : 'v',
  // 'w' : 'w',
  // 'x' : 'x',
  // 'y' : 'y',
  // 'z' : 'z',
  '0' : 'zero',
  '1' : 'one',
  '2' : 'two',
  '3' : 'three',
  '4' : 'four',
  '5' : 'five',
  '6' : 'six',
  '7' : 'seven',
  '8' : 'eight',
  '9' : 'nine'
};

function putFileInfo(filePath, fname, data) {
  var str = '"*/../' + filePath.slice(0,-4) + 'leb' + '"\n';
  
  // str +=  filePath + '\n';

  var name = fname.slice(0, -5);
  for (var i = 0; i < name.length; i++) {
    if(names[name[i]] != undefined ) { // skip a, b, c, d, e ...
      str += names[name[i]] + '\n';
    }
  }

  str += '.\n';

  // console.log(str)

  data.push(str);
}