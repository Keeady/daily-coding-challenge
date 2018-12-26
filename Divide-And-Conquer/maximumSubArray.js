function findMax(elements) {
    return findMaxSubArray(elements, 0, elements.length - 1);
}
//12,13,11,14,13,16
function findMaxSubArray(elements, low, high) {
    if (high == low) {
        return [low, high, elements[low]];
    }
    var mid = findMidPoint(low, high);
    var left = findMaxSubArray(elements, low, mid);
    var right = findMaxSubArray(elements, mid + 1, high);
    var cross = findMaxCrossSubArray(elements, low, mid, high);
    if (left[2] > right[2] && left[2] > cross[2]) {
        return left;
    }
    else if (right[2] > left[2] && right[2] > cross[2]) {
        return right;
    }
    else {
        return cross;
    }
}
function findMidPoint(low, high) {
    return Math.floor((low + high) / 2);
}
function findMaxCrossSubArray(elements, low, mid, high) {
    var maxLeftSum = Number.MIN_VALUE;
    var maxLeftIndex;
    var i = mid;
    var sum = 0;
    while (i >= 0) {
        sum += elements[i];
        if (sum > maxLeftSum) {
            maxLeftSum = sum;
            maxLeftIndex = i;
        }
        i--;
    }
    i = mid + 1;
    var maxRightSum = Number.MIN_VALUE;
    var maxRightIndex;
    sum = 0;
    while (i <= high) {
        sum += elements[i];
        if (sum > maxRightSum) {
            maxRightSum = sum;
            maxRightIndex = i;
        }
        i++;
    }
    return [maxLeftIndex, maxRightIndex, maxLeftSum + maxRightSum];
}
module.exports = findMax;
