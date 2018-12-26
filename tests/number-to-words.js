var test = require('unit.js');
var numberToWords = require('../String/integer-to-english-words');

var res = numberToWords(20);
test.value(res).is('twenty');

res = numberToWords(0);
test.value(res).is('zero');

res = numberToWords(100);
test.value(res).is('one hundred');

res = numberToWords(1000);
test.value(res).is('one thousand');

res = numberToWords(101);
test.value(res).is('one hundred one');

res = numberToWords(1001);
test.value(res).is('one thousand one');

res = numberToWords(1001001);
test.value(res).is('one million one thousand one');

res = numberToWords(1011011);
test.value(res).is('one million eleven thousand eleven');

res = numberToWords(4);
test.value(res).is('four');

res = numberToWords(24);
test.value(res).is('twenty four');

res = numberToWords(11);
test.value(res).is('eleven');

res = numberToWords(41);
test.value(res).is('forty one');

res = numberToWords(211);
test.value(res).is('two hundred eleven');

res = numberToWords(341);
test.value(res).is('three hundred forty one');

res = numberToWords(2341);
test.value(res).is('two thousand three hundred forty one');

res = numberToWords(12341);
test.value(res).is('twelve thousand three hundred forty one');

res = numberToWords(22341);
test.value(res).is('twenty two thousand three hundred forty one');

res = numberToWords(123341);
test.value(res).is('one hundred twenty three thousand three hundred forty one');

res = numberToWords(423341);
test.value(res).is('four hundred twenty three thousand three hundred forty one');

res = numberToWords(1413341);
test.value(res).is('one million four hundred thirteen thousand three hundred forty one');

res = numberToWords(1234567891);
test.value(res).is('one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety one');


