var test = require('unit.js');
var regexMatcher = require('../String/regexMatcher');
/*var text = "aa", pattern = "a";
var res = regexMatcher(text, pattern);
test.bool(res).isFalse();

text = "aa", pattern = "aa";
res = regexMatcher(text, pattern);
test.bool(res).isTrue();

text = "abc", pattern = "a.c";
res = regexMatcher(text, pattern);
test.bool(res).isTrue();

text = "abbb", pattern = "ab*";
res = regexMatcher(text, pattern);
test.bool(res).isTrue();

text = "acd", pattern = "ab*c.";
res = regexMatcher(text, pattern);
test.bool(res).isTrue();

text = "abcd", pattern = "ab*ce.";
res = regexMatcher(text, pattern);
test.bool(res).isFalse();

text = "abcd", pattern = "ab*cd.";
res = regexMatcher(text, pattern);
test.bool(res).isFalse();*/

var text = "", pattern = "a*";
var res = regexMatcher(text, pattern);
test.bool(res).isTrue();

text = "abaa", pattern = "a.*a*";
var res = regexMatcher(text, pattern);
test.bool(res).isTrue();
