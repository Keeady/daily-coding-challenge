function findElementSum(elements, sum) {
    var left = 0;
    var right = elements.length - 1;
    return search(elements, left, right, sum);
}
function search(elements, left, right, sum) {
    if (left > right) {
        return false;
    }
    var add = left + right;
    if (add < sum) {
        left += 1;
    }
    else if (add > sum) {
        right -= 1;
    }
    else {
        return true;
    }
    return search(elements, left, right, sum);
}
module.exports = findElementSum;
