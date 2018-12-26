var test = require('unit.js');
var kFrequentWords = require('../Most-Frequent-Words/findKFrequentWords');
var words = 'the brown fox likes the brown meat fox likes pie too';
var k = 4;

var res = kFrequentWords(words, k);
test.value(res).is({'the': 2, 'brown': 2, 'fox': 2, 'likes': 2});
