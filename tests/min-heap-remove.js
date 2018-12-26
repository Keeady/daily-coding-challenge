var test = require('unit.js');
var minHeapRemove = require('../Heap-sort/min-heap-remove');
var arr = [1, 2, 4, 5, 3, 6];
var res = minHeapRemove(arr);
test.value(res).is([2, 3, 4, 5, 6]);
