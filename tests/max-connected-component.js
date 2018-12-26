var test = require('unit.js');
var maxConnected = require('../Matrix/max-connected-component');
var matrix = [[0, 1, 1, 0], [0, 1,  0,  1], [1,  0,  1,  1], [0, 0, 0, 0],[1, 0, 0, 1]];

var max = maxConnected(matrix);
test.value(max).is(3);
