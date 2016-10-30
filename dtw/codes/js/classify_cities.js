var fs = require('fs');
var path = require('path');

var filesPath = './../../data/mandi/'

fs.readdir(filesPath, function (err, files) {
  if (err) console.log(err);
    files.forEach( function (file, index) {
      if (file.indexOf('.mfcc') != -1) {
        // console.log(file)
        // save files at the /processed directory
        var savePath = path.resolve('./../../data/processed');
        
        // create proper directory name
        var removeRE = /(([0-9]+)\_?)|(_+\.mfcc)|(.mfcc)|(_+([0-9]+)\.mfcc)/gi // 4561_ | 1345 | .mfcc | _.mfcc | __.mfcc | _4.mfcc

        var dirname = file.replace(removeRE, '') + '.mfcc';

        fs.writeFile(savePath+ 'test.txt', 'filesPath + file')

        var savePath = savePath + '/' + dirname; // where the file would be saved

        if (!fs.existsSync(savePath)) {
          fs.mkdirSync(savePath);
        }

        // console.log(file)

        // copy the file to appropriate directory    
        fs.createReadStream(filesPath + file).pipe(fs.createWriteStream(savePath + '/' + file));
        // fs.writeFile(filesPath + 'city.txt', );
        
        // console.log(filesPath + file)//, savePath + '/' + file)

      }
    })
})