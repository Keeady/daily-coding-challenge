var test = require('unit.js')
var findUnique = require('../String/first-Unique-Character');

var letter = 'leetcode';
var res = findUnique(letter);
test.value(res).is(0);

letter = 'deetcode';
res = findUnique(letter);
test.value(res).is(3);

letter = 'the brown chicken crossed the road. why?';
res = findUnique(letter);
test.value(res).is(4);
