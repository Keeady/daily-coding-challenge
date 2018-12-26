var test = require('unit.js');
var mergeSort = require('../Merge-sort/mergeSort');
var elements = [31,41, 59, 26, 42, 58];
mergeSort(elements);
test.array(elements).is([26, 31, 41, 42, 58, 59]);

elements = [8,5,7,6];
mergeSort(elements);
test.array(elements).is([5,6,7,8]);

elements = [8, 7, 6, 5];
mergeSort(elements);
test.array(elements).is([5,6,7,8]);
