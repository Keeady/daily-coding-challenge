function TrappingRainWater(arr) {
    if (arr.length < 3) {
        return 0;
    }

    //find left and right for each cell
    let left = buildLeftHeight(arr);
    let right = buildRightHeight(arr);

    // calculate height for each cell
    return calculateHeight(arr, left, right);
}

function buildLeftHeight(arr) {
    let height = [0];
    let maxLeft = arr[0];
    for (let i = 1; i < arr.length - 1; i++) {
        if (maxLeft < arr[i - 1]) {
            maxLeft = arr[i - 1];
        }

        height[i] = maxLeft;
    }

    return height;
}

function buildRightHeight(arr) {
    let height = [];
    let maxRight = arr[arr.length - 1];
    for (let i = arr.length - 2; i > 0; i--) {
        if (maxRight < arr[i + 1]) {
            maxRight = arr[i + 1];
        }

        height[i] = maxRight;
    }

    return height;
}

function calculateHeight(arr, left, right) {
    let height = 0;
    for (let i = 1; i < arr.length - 1; i++) {
        if (arr[i] >= left[i] || arr[i] >= right[i]) {
            continue;
        }

        height += Math.min(left[i], right[i]) - arr[i];
    }

    return height;
}

module.exports = TrappingRainWater;
