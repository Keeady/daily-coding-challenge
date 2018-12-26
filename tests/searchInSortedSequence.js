var test = require('unit.js');
var search = require('../Insertion-sort/searchInSortedSequence');
var elements = [26, 31, 41, 43, 58, 59];
var v = 26;
var result = search(elements, v);
test.value(result).is(0);

v = 265;
result = search(elements, v);
test.value(result).is(null);

v = 21;
result = search(elements, v);
test.value(result).is(null);

v = 58;
result = search(elements, v);
test.value(result).is(4);



