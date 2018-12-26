var removeDuplicate = require('../Remove-Dups/removeDupArray');
var removeDuplicateExt = require('../Remove-Dups/removeDupArrayExtended');
var test = require('unit.js');
var elemets = [1,3,4,5,6,4,6,7,2,5,7];
var result = removeDuplicate(elemets);
test.value(result).is([1,3,4,5,6,7,2]);

result = removeDuplicateExt(elemets);
test.value(result).is([1,3,4,5,6,7,2]);
