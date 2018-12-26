function productArrayV2(inputArray) {
    //product of left of i
    let left = [1];
    //product of right of i
    let right = [];
    right[inputArray.length - 1] = 1;
    let i;
    let output = [];

    for (i = 0; i < inputArray.length - 1; i++) {
        left[i + 1] = left[i] * inputArray[i];
    }

    for (i = inputArray.length - 1; i > 0; i--) {
        right[i - 1] = right[i] * inputArray[i];
    }

    for (i = 0; i < inputArray.length; i++) {
        output[i] = left[i] * right[i];
    }

    return output;
}

module.exports = productArrayV2;
