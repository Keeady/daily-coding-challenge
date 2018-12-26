var test = require('unit.js');
var findPairs = require('../Two-Element-Sum/findPairsWithGivenDifference');

var arr = [0, -1, -2, 2, 1], k = 1;
var res = findPairs(arr, k);

test.value(res).is([[1, 0], [0, -1], [-1, -2], [2, 1]]);
