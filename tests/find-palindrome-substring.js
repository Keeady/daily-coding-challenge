var test = require('unit.js');
var findPal = require('../String/find-palindrome-substring');

var s = 'abbcbba';
var res = findPal(s);
var expected = ['abbcbba', 'bb', 'bcb', 'bbcbb'];
var result = {};
res.forEach((r) => {
    result[r] = true;
});

expected.forEach((e) => {
    test.bool(result[e]).isTrue();
});

s = 'abxybxzcbsuba';
res = findPal(s);
test.value(res.length).is(0);
