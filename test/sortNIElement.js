var test = require('unit.js');
var insertionSort = require('../Insertion-sort/insertionSortNonIncrementing');
var elements = [31,41, 59, 26, 41, 58];
insertionSort(elements);
test.array(elements).is([59, 58, 41, 41, 31, 26]);
