var matrixMult = require('../Divide-And-Conquer/squareMatrixMultiplication');
var test = require('unit.js');
var left = [[1, 2], [3, 4]];
var right = [[7, 8], [9, 10]];

var result = matrixMult(left, right);
test.value(result[0][0]).is(25);
test.value(result[0][1]).is(28);
test.value(result[1][0]).is(57);
test.value(result[1][1]).is(64);
