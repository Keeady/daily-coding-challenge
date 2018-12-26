var test = require('unit.js');
var reverseString = require('../String/reverse-string');
var input = "hello world";
var result = reverseString(input);
test.value(result).is("dlrow olleh");

input = "A man, a plan, a canal: Panama";
result = reverseString(input);
test.value(result).is("amanaP :lanac a ,nalp a ,nam A");
