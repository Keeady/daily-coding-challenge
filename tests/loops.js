var test = require('unit.js');

function testfor() {
    let i = 0;
    for (i = 0; i < 4; i++) {
        if (i === 1) {
            return false;
        }

    }

    return true;
}

function testwhile() {
    let i = 0;
    while(i < 4) {
        if (i === 1) {
            return true;
        }
        i++;
    }

    return false;
}

function testBreak() {
    let i = 0;
    while(i < 4) {
        if (i === 1) {
            break;
        }
        i++;
    }

    return false;
}

function testforbreak() {
    let i = 0;
    for (i = 0; i < 4; i++) {
        if (i === 1) {
            break;
        }

    }

    return true;
}

function testforreturn() {
    let i = 0;
    for (i = 0; i < 4; i++) {
        if (i === 1) {
            return;
        }

    }

    return true;
}

var res = testfor();
test.bool(res).isFalse();
res = testwhile();
test.bool(res).isTrue();
res = testBreak();
test.bool(res).isFalse();
res = testforbreak();
test.bool(res).isTrue();
res = testforreturn();
test.value(res).isUndefined();
