var fs = require('fs');
var path = require('path');

var rootPath = './../../data/processed/'

fs.readdir(rootPath, function (err, files) {
  if (err) console.log(err);
  files.forEach( function (dpath, index) {
    var filesPath =  rootPath + dpath;
    fs.stat(filesPath, function (err, stats) {
      // console.log(dpath)
      if(stats.isDirectory()) {
        fs.readdir(filesPath, function (err, mfccFiles) {
          if(mfccFiles.length<20) {
            // console.log(filesPath)
            deleteFolderRecursive(filesPath);
            console.log('Removed ' +filesPath + ' with file count -> ' + mfccFiles.length)
          }
        }) // ./readdir
      }
    }) // ./fs.stat
  })
}) // ./readdir


var deleteFolderRecursive = function(path) {
  if( fs.existsSync(path) ) {
      fs.readdirSync(path).forEach(function(file) {
        var curPath = path + "/" + file;
          if(fs.statSync(curPath).isDirectory()) { // recurse
              deleteFolderRecursive(curPath);
          } else { // delete file
              fs.unlinkSync(curPath);
          }
      });
      fs.rmdirSync(path);
    }
};