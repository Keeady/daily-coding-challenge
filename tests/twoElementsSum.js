var test = require('unit.js');
var twoElementsSum = require('../Two-Element-Sum/twoElementSum');
var elements = [1,2,3,4,5,6,7,8,9];
var sum = 12;
var result = twoElementsSum(elements, sum);
test.bool(result).isTrue();
