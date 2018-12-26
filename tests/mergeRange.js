var test = require('unit.js');
var mergeRange = require('../Array/mergeRanges');
var range = [[2, 5],[4, 8],[10, 12]];

var res = mergeRange(range);
test.value(res).is([[2,8], [10,12]]);

res = mergeRange([]);
test.value(res).is([]);

res = mergeRange([[2, 5], [4, 8], [7, 12]]);
test.value(res).is([[2, 12]]);

res = mergeRange([[1,3], [2,4], [5,7], [6,8]]);
test.value(res).is([[1, 4], [5, 8]]);

res = mergeRange([[6,8], [1, 9], [2, 4], [4, 7]]);
test.value(res).is([[1, 9]]);
