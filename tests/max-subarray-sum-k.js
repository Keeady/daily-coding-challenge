var test = require('unit.js');
var maxSubArraySumK = require('../Divide-And-Conquer/max-subarray-sum-k');

var arr = [1, 2, 1, -1, 1];
var k = 3;

var res = maxSubArraySumK(arr, k);
test.value(res).is(4);

arr = [1, 2, 1, -1, 2];
res = maxSubArraySumK(arr, 4);
test.value(res).is(4);

arr = [1, 2, 1, -1, 2];
res = maxSubArraySumK(arr, 2);
test.value(res).is(3);

arr = [1, 2, 1, -1, 2];
res = maxSubArraySumK(arr, 5);
test.value(res).is(5);

arr = [1, 2, 1, -1, 2];
res = maxSubArraySumK(arr, 10);
test.value(res).is(0);
