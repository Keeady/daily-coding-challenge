var test = require('unit.js');
var islandCount = require('../Matrix/islandCount');
var binaryMatrix = [ [0,    1,    0,    1,    0],
    [0,    0,    1,    1,    1],
    [1,    0,    0,    1,    0],
    [0,    1,    1,    0,    0],
    [1,    0,    1,    0,    1] ];

var res = islandCount(binaryMatrix);
test.value(res).is(6);
