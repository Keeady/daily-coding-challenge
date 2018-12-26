var test = require('unit.js');
var countIncorrectParentheses = require('../String/countIncorrectParentheses');
var input = '{(){}}';
var result = countIncorrectParentheses(input);
test.value(result).is(0);

input = '{(){}[(})}';
result = countIncorrectParentheses(input);
test.value(result).is(2);

input = '((())[{{{})';
result = countIncorrectParentheses(input);
test.value(result).is(4);


