var test = require('unit.js');
var getDifferentNumber = require('../MinMax/getDifferentNumber');

var arr = [0,1,2,3, 5];
var result = getDifferentNumber(arr);
test.value(result).is(4);

arr = [0,1,2,3];
result = getDifferentNumber(arr);
test.value(result).is(4);

arr = [400];
result = getDifferentNumber(arr);
test.value(result).is(0);

arr = [0,400];
result = getDifferentNumber(arr);
test.value(result).is(1);

arr = [0,1, 400];
result = getDifferentNumber(arr);
test.value(result).is(2);
