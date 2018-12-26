function TrappingRainWater(arr) {
    if (arr.length < 3) {
        return 0;
    }
    //l=0 r=0
    //[0,1,0,2*,1*,0*,1*,3*,2*,1*,2*,1]
    //[0,0] r=2 r=3
    // [1,2] r=3
    // [1,1]  r=3
    // [2, 0] r=1 r=3
    // [2, 1] r=3
    //[2, 3]
    //[2, 2]
    //[3, 1] r=2
    //[3, 2]
    //[3, 1]
    //[0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0
    //find left and right for each cell
    var heightMap = buildHeighMap(arr);
    // calculate height for each cell
    return calculateHeight(arr, heightMap);
}
function buildHeighMap(arr) {
    var left = arr[0], maxRight = arr[2];
    var heightMap = new Map();
    for (var i = 1; i < arr.length - 1; i++) {
        heightMap.set(i, [left, arr[i + 1]]);
        if (arr[i - 1] > left) {
            left = arr[i - 1];
            var current = heightMap.get(i);
            current[0] = left;
            heightMap.set(i, current);
        }
        if (arr[i + 1] > maxRight) {
            maxRight = arr[i + 1];
            var j = i - 1;
            while (arr[j + 1] < maxRight && j > 0) {
                var current = heightMap.get(j);
                current[1] = maxRight;
                heightMap.set(j, current);
                j--;
            }
        }
        else {
            maxRight = arr[i + 1];
        }
    }
    return heightMap;
}
function calculateHeight(arr, heightMap) {
    var height = 0;
    for (var i = 1; i < arr.length - 1; i++) {
        var leftRight = heightMap.get(i);
        var left = leftRight[0];
        var right = leftRight[1];
        if (arr[i] >= left || arr[i] >= right) {
            continue;
        }
        height += Math.min(left, right) - arr[i];
    }
    return height;
}
module.exports = TrappingRainWater;
