var test = require('unit.js');
var trap = require('../Array/trappingRainWater');

var arr = [0,1,0,2,1,0,1,3,2,1,2,1];
var res = trap(arr);
test.value(res).is(6);


