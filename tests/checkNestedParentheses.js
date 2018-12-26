var test2 = require('unit.js');
var checkNestedParentheses = require('../String/checkNestedParentheses');
var input = '{(){}}';
var result = checkNestedParentheses(input);
test2.bool(result).isTrue();

input = '{(){}[}}';
result = checkNestedParentheses(input);
test2.bool(result).isFalse();

input = '(((((((()))[][]{{{{{}}}}}})';
result = checkNestedParentheses(input);
test2.bool(result).isFalse();

input = ')()';
result = checkNestedParentheses(input);
test2.bool(result).isFalse();

