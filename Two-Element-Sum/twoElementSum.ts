function findElementSum(elements: number[], sum: number) {
    let left = 0;
    let right = elements.length - 1;
    return search(elements, left, right, sum);
}

function search(elements: number[], left: number, right: number, sum: number) {
    if (left > right) {
        return false;
    }

    let add = left + right;
    if (add < sum) {
        left += 1;
    } else if (add > sum) {
        right -= 1;
    } else {
        return true;
    }

    return search(elements, left, right, sum);
}

module.exports = findElementSum;
