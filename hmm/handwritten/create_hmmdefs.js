var fs = require('fs');

var MAX_ITER=10;
var digits = ['a', 'ai', 'bA', 'chA', 'dA', 'lA', 'tA'];
var hmmsPath = './io/hmms/'

var dump="";
digits.forEach((digit)=>{
  var hmmPath = hmmsPath + digit + '/' + 'hmm' + MAX_ITER + '/proto'
  var data = fs.readFileSync(hmmPath, 'utf-8');
  var index = data.indexOf('proto');
  var first = data.slice(0, index);
  var second = data.slice( index + 'proto'.length );
  dump += first + digit + second+'\n';
})

fs.writeFileSync(hmmsPath + 'hmmdefs', dump);