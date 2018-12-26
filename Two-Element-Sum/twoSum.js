function twoSum(inputArray, target) {
    //x + y = target
    // x = target - y;
    // add ele in map y -> i
    // find x, i of y != map.get(y)\
    if (inputArray.length <= 1) {
        return [];
    }
    var map = new Map();
    for (var i = 0; i < inputArray.length; i++) {
        if (map.has(inputArray[i]) && map.get(inputArray[i]) != i) {
            return [i, map.get(inputArray[i])];
        }
        map.set(target - inputArray[i], i);
    }
    return [];
}
module.exports = twoSum;
