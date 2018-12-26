function findMax(elements: number[]) {
    return findMaxSubArray(elements, 0, elements.length - 1);
}
//12,13,11,14,13,16
function findMaxSubArray(elements: number[], low: number, high: number) {
    if (high == low) {
        return [low, high, elements[low]]
    }

    let mid = findMidPoint(low, high);
    let left = findMaxSubArray(elements, low, mid);
    let right = findMaxSubArray(elements, mid + 1, high);
    let cross = findMaxCrossSubArray(elements, low, mid, high);

    if (left[2] > right[2] && left[2] > cross[2]) {
        return left;
    } else if (right[2] > left[2] && right[2] > cross[2]) {
        return right;
    } else {
        return cross;
    }
}

function findMidPoint(low, high) {
    return Math.floor((low + high) / 2);
}

function findMaxCrossSubArray(elements: number[], low: number, mid:number, high: number) {
    let maxLeftSum = Number.MIN_VALUE;
    let maxLeftIndex;
    let i = mid;
    let sum = 0;
    while (i >= 0) {
        sum += elements[i];
        if (sum > maxLeftSum) {
            maxLeftSum = sum;
            maxLeftIndex = i;
        }
        i--;
    }

    i = mid + 1;
    let maxRightSum = Number.MIN_VALUE;
    let maxRightIndex;
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
