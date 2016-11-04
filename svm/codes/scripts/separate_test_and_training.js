var fs = require('fs');
var path = require('path');
var _ = require('underscore')

var dirPaths = [
  '../../data/given/coast/',
  '../../data/given/forest/',
  '../../data/given/highway/',
  '../../data/given/insidecity/',
  '../../data/given/mountain/',
  '../../data/given/opencountry/',
  '../../data/given/street/',
  '../../data/given/tallbuildings/'
]

var types = [
  'coast', 'forest', 'highway', 'insidecity', 
  'mountain', 'opencountry', 'street', 'tallbuildings'
]
var testSaveRoot = '../../data/processed/test/'
var trainSaveRoot = '../../data/processed/train/'

dirPaths.forEach((dir, index)=>{
  var testPaths = [];
  var trainPaths = [];
  var filesList = fs.readdirSync(dir);
  filesList = _.shuffle(filesList);
  var type = whichType(dir);

  var testCount = Math.floor(0.25 * filesList.length);

  for (var i = 0; i < testCount; i++) {
    var fname = filesList[i];
    var fPath = path.resolve(__dirname, dir, fname); 
    testPaths.push(fPath);
  }

  for (var i = testCount, j = filesList.length; i < j; i++) {
    var fname = filesList[i];
    var fPath = path.resolve(__dirname, dir, fname);  
    trainPaths.push(fPath);
  }
  console.log(testPaths)
  console.log(testSaveRoot+type+'.txt')
  // create a new test file which will contain all files path
  fs.writeFileSync(testSaveRoot+type+'.txt', testPaths.join('\n'));

  // create a new train file which will contain all files path
  fs.writeFileSync(trainSaveRoot+type+'.txt', trainPaths.join('\n'));
})



function whichType(dir) {
    var type = types.reduce((store, el)=>{
    if(dir.indexOf(el) > -1){
      return store = el;
    } else {
      return store;
    }
  })
  return type;
}