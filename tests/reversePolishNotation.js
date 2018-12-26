var test = require('unit.js');
var reversePolishNotation = require('../Array/reversePolishNotation');

var arr = ["2", "1", "+", "3", "*"];
var res = reversePolishNotation(arr);
test.value(res).is(9);

arr = ["4", "13", "5", "/", "+"];
res = reversePolishNotation(arr);
test.value(res).is(6);

arr = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"];
res = reversePolishNotation(arr);
test.value(res).is(22);
