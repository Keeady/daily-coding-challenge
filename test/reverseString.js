var test = require('unit.js');
var reverseString = require('../String/reverseString');
var input = "hello world";
var result = reverseString(input);
test.value(result).is("dlrow olleh");
