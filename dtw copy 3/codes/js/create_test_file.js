var fs = require('fs');
var path = require('path');
var _ = require('underscore');

var rootPath = './../../data/test/';
var testPath = './../../data/test-1/'

fs.readdir(rootPath, function (err, files) {
  if (err) console.log(err);
  files.forEach( function (dpath, index) {
    var filesPath =  rootPath + dpath;  
    fs.stat(filesPath, function (err, stats) {
      // console.log(dpath)
      if(stats.isDirectory()) {
        fs.readdir(filesPath, function (err, mfccFiles) {
          var testCount = Math.floor(mfccFiles.length * 0.5);
          var range = _.range(testCount)
          range = _.shuffle(range);
          for (var i = testCount - 1; i >= 0; i--) {
            var place = range[i];
            var delPath = filesPath + '/' + mfccFiles[place];
            var savePath = testPath + dpath + '/' + mfccFiles[place]
            // console.log(place, mfccFiles.length, delPath ,savePath);
            if (!fs.existsSync(testPath + dpath)) {
              fs.mkdirSync(testPath + dpath);
            }

            fs.createReadStream(delPath).pipe(fs.createWriteStream(savePath));
            // fs.unlink(delPath, function (err) {
            //   if (err) console.log(err);
            // })
            
          }
          console.log('\n');
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