function findArrayQuadruplet(arr, s) {
    // a +b +c + d = s
    // a + b = s - (c + d)
    if (arr.length < 4) {
        return [];
    }
    arr.sort();
    for (var i = 0; i < arr.length - 4; i++) {
        for (var x = i + 1; x < arr.length - 3; x++) {
            var s2 = s - (arr[i] + arr[x]);
            var low = x + 1;
            var high = arr.length - 1;
            while (low < high) {
                if (arr[low] + arr[high] < s2) {
                    low++;
                }
                else if (arr[low] + arr[high] > s2) {
                    high--;
                }
                else {
                    return [arr[i], arr[x], arr[low], arr[high]];
                }
            }
        }
    }
    return [];
}
module.exports = findArrayQuadruplet;
