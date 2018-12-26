function maxSubArraySumK(inputArray, k) {
    let i;
    let max = 0;
    // Map stores sum from 0 to i and index i
    let rangeSum = new Map();
    //For sum sub array starting from 0 to get the correct length
    rangeSum.set(0, -1);

    buildRangeSum(inputArray);

    for (i = 0; i < inputArray.length; i++) {
        if (rangeSum.has(inputArray[i] - k)) {
            //right index - left index
            max = Math.max(max, i - rangeSum.get(inputArray[i] - k));
        }

        if (!rangeSum.has(inputArray[i])) {
            rangeSum.set(inputArray[i], i);
        }
    }

    return max;
}

/**
 * Sum(i) = sum of the range 0 to i
 * @param inputArray
 * @return {any}
 */
function buildRangeSum(inputArray) {
    let i;
    for (i = 1; i < inputArray.length; i++) {
        inputArray[i] += inputArray[i - 1];
    }

    return inputArray;
}

module.exports = maxSubArraySumK;
