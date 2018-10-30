var test = require('unit.js');
var maxSubArray = require('../Divide-And-Conquer/maximumSubArray');
var elements = [-2, -3, 4, -1, -2, 1, 5, -3];
var result = maxSubArray(elements);
test.value(result).isNotEmpty();
