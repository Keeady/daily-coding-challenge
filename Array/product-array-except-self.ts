function productArray(inputArray) {
    let i;
    let j;
    let output = [];

    for (i = 0; i < inputArray.length; i++) {
        output[i] = 1;
        for (j = 0; j < inputArray.length; j++) {
            if (i !== j) {
                output[i] *= inputArray[j];
            }
        }
    }

    return output;
}

module.exports = productArray;
