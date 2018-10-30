var test = require('unit.js');
var search = require('../Insertion-sort/searchInSequence');
var elements = [31,41, 59, 26, 41, 58];
var v = 26;
var result = search(elements, v);
test.value(result).is(3);

v = 265;
result = search(elements, v);
test.value(result).is(null);
