var test = require('unit.js');
var isPal = require('../String/is-palindrome');

var s = 'abba';
var res = isPal(s);
test.bool(res).isTrue();

s = 'abcba';
res = isPal(s);
test.bool(res).isTrue();

s = 'abvcba';
res = isPal(s);
test.bool(res).isFalse();

s = 'abad';
res = isPal(s);
test.bool(res).isFalse();
