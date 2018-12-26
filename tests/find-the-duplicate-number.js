var test = require('unit.js');
var findDup = require('../Array/find-the-duplicate-number');

var arr = [1,3,4,2,2];
var res = findDup(arr);
test.value(res).is(2);

arr = [3,1,3,4,2];
res = findDup(arr);
test.value(res).is(3);

arr = [1, 5, 5, 2, 4, 3, 6];
res = findDup(arr);
test.value(res).is(5);
