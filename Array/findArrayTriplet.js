function findArrayTriplet(arr, s) {
    if (arr.length < 3) {
        return [];
    }
    // a + b + c = s
    // b + c = s - a
    arr.sort();
    for (var i = 0; i < arr.length - 3; i++) {
        var s2 = s - arr[i];
        var low = i + 1;
        var high = arr.length - 1;
        while (low < high) {
            if (arr[low] + arr[high] < s2) {
                low++;
            }
            else if (arr[low] + arr[high] > s2) {
                high--;
            }
            else {
                return [arr[i], arr[low], arr[high]];
            }
        }
    }
    return [];
}
module.exports = findArrayTriplet;
