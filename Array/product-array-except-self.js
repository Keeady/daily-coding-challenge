function productArray(inputArray) {
    var i;
    var j;
    var output = [];
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
