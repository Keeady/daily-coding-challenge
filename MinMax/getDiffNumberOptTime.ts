function getDifferentNumber(inputAray) {
    let length = inputAray.length;
    let map = new Map();
    let index;
    for (index = 0; index < length; index++) {
        map.set(index, true);
    }

}

module.exports = getDifferentNumber;
