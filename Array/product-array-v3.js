function productArrayV3(inputArray) {
    var temp = 1;
    var output = [1];
    var i;
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
