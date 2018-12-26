var test = require('unit.js');
var insertionSort = require('../Insertion-sort/insertionSortBinarySearch');
var elements = [31,41, 59, 26, 41, 58];
insertionSort(elements);
test.array(elements).is([26, 31, 41, 41, 58, 59]);
