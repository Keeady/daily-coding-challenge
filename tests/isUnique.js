var test = require('unit.js');
var isUnique = require('../isUnique/isUnique.js');
var isUniqueExtended = require('../isUnique/isUniqueExtended.js');
test.bool(isUnique('camelijio')).isFalse();
test.bool(isUnique('camaria')).isFalse();
test.bool(isUnique('   ')).isTrue();
test.bool(isUnique('d')).isTrue();
test.bool(isUnique('abc defg hijkl mnopqr stuvwxy z1234 %56789*.#')).isTrue();
test.bool(isUnique('abc defg hijkl mnopxr stuvwxy z1234 %56789*.#')).isFalse();

test.bool(isUniqueExtended('camelijio')).isFalse();
test.bool(isUniqueExtended('camaria')).isFalse();
test.bool(isUniqueExtended('   ')).isTrue();
test.bool(isUniqueExtended('d')).isTrue();
test.bool(isUniqueExtended('abc defg hijkl mnopqr stuvwxy z1234 %56789*.#')).isTrue();
test.bool(isUniqueExtended('abc defg hijkl mnopxr stuvwxy z1234 %56789*.#')).isFalse();


