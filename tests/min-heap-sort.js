var test = require('unit.js');
var minSort = require('../Heap-sort/min-heap-sort');
var arr = [13, 14, 8];
var res = minSort(arr);
test.value(res).is([8, 14, 13]);

arr = [4, 10, 3, 5, 1];
//4, 10, 1, 5, 3
// 4, 3, 1, 5, 10
//1, 3, 4, 5, 10
res = minSort(arr);
test.value(res).is([1, 3, 4, 5, 10]);

arr = [3, 1, 6, 5, 2, 4];
res = minSort(arr);
test.value(res).is([1, 2, 4, 5, 3, 6]);

//6,
