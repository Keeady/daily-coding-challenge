var test = require('unit.js');
var reverse = require('../String/reverse-string-ii');
var s = 'abcdefg', k=2;

var res = reverse(s, k);
test.value(res).is('bacdfeg');

s = 'abcdefgh';
res = reverse(s, k);
test.value(res).is('bacdfegh');

s = 'abcdefghi';
res = reverse(s, k);
test.value(res).is('bacdfeghi');

s = 'abcdefghijk';
res = reverse(s, k);
test.value(res).is('bacdfeghjik');

s = 'ab';
res = reverse(s, k);
test.value(res).is('ba');

s = 'abc';
res = reverse(s, k);
test.value(res).is('bac');

s = 'abcd';
res = reverse(s, k);
test.value(res).is('bacd');
