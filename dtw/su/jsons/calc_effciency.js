var _ = require('underscore');
var fs = require('fs');
var path = require('path');

var data_1 = require('./result_1_bkp.json');
var data_2 = require('./result_2_bkp.json');
var data_3 = require('./result_3_bkp.json');
var data_4 = require('./result_4_bkp.json');

data = [];
// console.log(data.length)
data = data.concat(data_1);
// console.log(data.length)
data = data.concat(data_2);
// console.log(data.length)
data = data.concat(data_3);
// console.log(data.length)
// data = data.concat(data_4);
// console.log(data_4.length)

var removeRE = /(([0-9]+)\_?)|(_+\.mfcc)|(.mfcc)|(_+([0-9]+)\.mfcc)/gi // 4561_ | 1345 | .mfcc | _.mfcc | __.mfcc | _4.mfcc
var specialSymRe = /\'/gi;

// var unique = _.uniq(data);
 var efficiency = 0;
for (var i = 0; i < data.length; i++) {
  var item = data[i];
  for(var key in item){
    if(key!=='dist'){
      var val = item[key];

      var base = path.basename(key);
      var identified = path.basename(val);

      var testCityName = base.replace(removeRE, '');
      var identifiedCityName = identified.replace(removeRE, '');
      // console.log(testCityName, identifiedCityName)
      if(testCityName == identifiedCityName){
        efficiency++;
        console.log('true');
      }else {
        console.log('false');
      }
    }
  }
}

console.log(efficiency/data.length)



