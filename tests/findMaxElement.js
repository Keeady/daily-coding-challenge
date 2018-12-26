var test = require('unit.js');
var findMax = require('../MinMax/maxElementInArray');
var input = [-20, -4, -1, -14, -9, -2];
var result = findMax(input);
test.value(result).is(-1);

input = [-20, -4, -1, -14, -9, -2];
var result = findMax(input);
test.value(result).is(-1);

input = [-20, -4, -1, -14, -9, -2, 0];
result = findMax(input);
test.value(result).is(0);

input = [20, 4, 1, 14, 9, 2];
result = findMax(input);
test.value(result).is(20);

input = [-20, 4, 1, -14, -9, -2, 20];
result = findMax(input);
test.value(result).is(20);
