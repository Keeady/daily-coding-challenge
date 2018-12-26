var test = require('unit.js');
var product = require('../Array/product-array-v3');

var input = [1,2,3,4];
var res = product(input);
test.value(res).is([24,12,8,6]);

input = [2,3,4,5];
res = product(input);
test.value(res).is([60, 40, 30, 24]);
