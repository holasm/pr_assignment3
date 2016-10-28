var fs = require('fs');
var path =  require('path');
var _ = require('lodash');

// var letters = 'abcdefghijklmnopqrstuvwxyz';
var digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

// file paths
var wlistFile = './../io/created/wlist'
var lexiconFile = './../io/created/lexicon'
var grammerFile = './../io/created/grammer'

// combine all letters and digits

var data = '';
var all = [];
// for (var i = 0; i < letters.length; i++) {
//   all.push(letters[i]);
// }

// var all = all.concat(digits);
var all = digits;
all = all.sort();

data += all[0];
for (var i = 1; i < all.length; i++) {
  data += ' | ' + all[i];
}
data = '$data = ' + data + ';\n';
data += '( SENT-START ( <$data> ) SENT-END )';

fs.writeFile(grammerFile, data);

// create lexison
var lexicon = '';
for (var i = 0; i < all.length; i++) {
  lexicon += wordWlist(all[i], all[i], 15) + '\n';
}

lexicon += wordWlist('sent-start', 'sil', 15) + '\n';
lexicon += wordWlist('sent-end', 'sil', 15) + '\n';

fs.writeFile(lexiconFile, lexicon);

function createSpace(count) {
  var spaces = '';
  for (var i = count - 1; i >= 0; i--) {
    spaces += ' '
  }
  return spaces;
}

function wordWlist(word1, word2, maxSpace) {
  var spaces = '';
  spaces = createSpace(maxSpace);
  spaces = spaces.slice(0, -word1.length);
  return word1 + spaces + word2;
}

// create wlist

var wlist = '';
for (var i = 0; i < all.length; i++) {
  wlist += all[i] + '\n';
}

wlist += 'sil' + '\n';
wlist += 'sil' + '\n';

fs.writeFile(wlistFile, wlist);