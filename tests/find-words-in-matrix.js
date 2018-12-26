var test = require('unit.js');
var findWords = require('../Matrix/find-words-in-matrix');
var words = [['a', 'g', 'i', 'w', 't'], ['x', 'l', 'o', 'a', 's'], ['i', 'o', 'n', 't', 'i'], ['s', 'w', 'e', 'l', 'l']];
var expected = ['wig', 'twig', 'axis', 'swell', 'list', 'one', 'glow', 'six', 'well', 'ion', 'lew', 'on'];
var unexpected = ['sweat', 'enlist', 'ones'];
var res = findWords(words, expected);
expected.forEach((w) => {
    test.bool(res[w]).isTrue();
});

res = findWords(words, unexpected);
unexpected.forEach((w) => {
    test.bool(res[w]).isFalse();
});
