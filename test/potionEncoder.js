var potionEncoder = require('../Hermiones-potion/potionEncoder.js');
var test = require('unit.js');
test.assert('AB*C*', potionEncoder('ABABCABABC'));
test.assert('AB*', potionEncoder('ABAB'));
test.assert('ABCD', potionEncoder('ABCD'));
test.assert('AB*C*DEF*', potionEncoder('ABABCABABCDEFABABCABABCDEF'));
test.assert('A', potionEncoder('A'));
test.assert('AB', potionEncoder('AB'));


