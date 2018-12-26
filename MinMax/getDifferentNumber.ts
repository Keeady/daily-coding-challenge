function getDifferentNumber(inputAray) {
    //sort input
    inputAray.sort();
    let index;
    let min = 0;

    //iterate and find the distance between conseq numbers
    for (index = 0; index < inputAray.length; index++) {
        if ((inputAray[index] - min) >= 1) {
            return min;
        }

        min = inputAray[index] + 1;
    }
    //if distance > 1, min is left + 1

    return min;
}

module.exports = getDifferentNumber;
