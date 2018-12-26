var test = require('unit.js');
var findArrayTriplet = require('../Array/findArrayTriplet');

var arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20;
var res = findArrayTriplet(arr, s);
test.value(res).is([4, 7, 9]);
