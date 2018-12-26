var test = require('unit.js');
var minHeapInsert = require('../Heap-sort/min-heap-insert');
var arr = [1, 2, 4, 5, 3, 6];
var res = minHeapInsert(arr, 8);
test.value(arr).is([1, 2, 4, 5, 3, 6, 8]);
test.value(res).is(6);

arr = [1, 3, 4, 5, 10];
res = minHeapInsert(arr, 2);
test.value(arr).is([1, 3, 2, 5, 10, 4]);
test.value(res).is(2);
