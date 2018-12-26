function TrappingRainWater(arr) {
    if (arr.length < 3) {
        return 0;
    }
    //find left and right for each cell
    var left = buildLeftHeight(arr);
    var right = buildRightHeight(arr);
    // calculate height for each cell
    return calculateHeight(arr, left, right);
}
function buildLeftHeight(arr) {
    var height = [0];
    var maxLeft = arr[0];
    for (var i = 1; i < arr.length - 1; i++) {
        if (maxLeft < arr[i - 1]) {
            maxLeft = arr[i - 1];
        }
        height[i] = maxLeft;
    }
    return height;
}
function buildRightHeight(arr) {
    var height = [];
    var maxRight = arr[arr.length - 1];
    for (var i = arr.length - 2; i > 0; i--) {
        if (maxRight < arr[i + 1]) {
            maxRight = arr[i + 1];
        }
        height[i] = maxRight;
    }
    return height;
}
function calculateHeight(arr, left, right) {
    var height = 0;
    for (var i = 1; i < arr.length - 1; i++) {
        if (arr[i] >= left[i] || arr[i] >= right[i]) {
            continue;
        }
        height += Math.min(left[i], right[i]) - arr[i];
    }
    return height;
}
module.exports = TrappingRainWater;
