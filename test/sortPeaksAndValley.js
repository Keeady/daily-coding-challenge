var sortPeaksAndValley = require('../Peaks-And-Valley/peaksAndValley');
var test = require('unit.js');
var input = [2,3,4,5,6];
var output = [2,4,3,6,5];
var expOutput = sortPeaksAndValley(input);
test.array(output).is(expOutput);

input = [2,9,0,1,4,6,3];
output = [2,9,0,4,1,6,3];
expOutput = sortPeaksAndValley(input);
test.array(output).is(expOutput);

input = [2];
output = [2];
expOutput = sortPeaksAndValley(input);
test.array(output).is(expOutput);

input = [];
output = [];
expOutput = sortPeaksAndValley(input);
test.array(output).is(expOutput);

input = [2,9];
output = [2,9];
expOutput = sortPeaksAndValley(input);
test.array(output).is(expOutput);
