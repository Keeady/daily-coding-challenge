var test = require('unit.js');
var findArrayQuandruplet = require('../Array/findArrayQuandruplet');

var arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20;
var res = findArrayQuandruplet(arr, s);
test.value(res).is([0, 4, 7, 9]);
