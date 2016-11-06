var fs = require('fs');
var _ = require('underscore');

var data1 = fs.readFileSync('./../../data/processed/test.txt', 'utf-8');
var data2 = fs.readFileSync('./../../data/processed/test_1.txt', 'utf-8');

// console.log(data1.split('\n'))
// console.log(data2.split('\n'))
// console.log(data2)

var data3 = _.difference(data1.split('\n'), data2.split('\n'));
var data4 = '';

data3.forEach((data)=>{
  data4 += '\n';
  data4 += '\"';
  data4 += data;
  data4 += '\"';
})

fs.writeFileSync('./../../data/processed/test_2.txt', data4);

