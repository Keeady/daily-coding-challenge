var test = require('unit.js');
var compare = require('../String/compare-version-space');
var v1 = '1.0.1';
var v2 = '1';

var res = compare(v1, v2);
test.value(res).is(1);

v1 = '0.1';
v2 = '1.0.1';

res = compare(v1, v2);
test.value(res).is(-1);

v1 = '7.5.2.4';
v2 = '7.5.3';

res = compare(v1, v2);
test.value(res).is(-1);

v1 = '1.5.2.4';
v2 = '2.0';

res = compare(v1, v2);
test.value(res).is(-1);

v1 = '7.5.2.4';
v2 = '7.5.2.4';

res = compare(v1, v2);
test.value(res).is(0);

v1 = '7.5.2.4';
v2 = '8';

res = compare(v1, v2);
test.value(res).is(-1);

v1 = '17.45.12.4';
v2 = '17.45.12.4.0';

res = compare(v1, v2);
test.value(res).is(0);

v1 = '17.45.12.4';
v2 = '17.45.12.4.0.0.0';

res = compare(v1, v2);
test.value(res).is(0);

v1 = '10.6.5';
v2 = '10.6';

res = compare(v1, v2);
test.value(res).is(1);
