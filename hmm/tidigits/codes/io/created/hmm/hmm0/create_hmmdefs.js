var fs = require('fs');

var classes = ['zero','one','two','three','four','five','six','seven','eight','nine', 'sil', 'oh'];

var data = '';

fs.readFile('proto', 'utf-8', function (err, fileData) {
  if(err) new Error(err);
  classes.sort().forEach(function (el ,index) {
    // fs.writeFile('./../models0/' + el, fileData.replace('proto', el)); // create models0 directory
    data += fileData.replace('proto', el) + '\n'; // concat proto for different symbols
  })

  fs.writeFile('hmmdefs', data);
})