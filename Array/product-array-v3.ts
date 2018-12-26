function productArrayV3(inputArray) {
    let temp = 1;
    let output = [1];
    let i;

    for (i = 0; i < inputArray.length - 1; i++) {
        output[i + 1] = output[i] * inputArray[i];
    }

    for (i = inputArray.length - 1; i > 0; i--) {
        temp *= inputArray[i];
        output[i - 1] *= temp;
    }

    return output;
}

module.exports = productArrayV3;
