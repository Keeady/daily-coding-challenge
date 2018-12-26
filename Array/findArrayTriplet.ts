function findArrayTriplet(arr, s) {
    if (arr.length < 3) {
        return [];
    }

    // a + b + c = s
    // b + c = s - a

    arr.sort();
    for (let i = 0; i < arr.length - 3; i++) {
        let s2 = s - arr[i];
        let low = i + 1;
        let high = arr.length - 1;

        while (low < high) {
            if (arr[low] + arr[high] < s2) {
                low++;
            } else if (arr[low] + arr[high] > s2) {
                high--;
            } else {
                return [arr[i], arr[low], arr[high]];
            }
        }
    }

    return [];
}

module.exports = findArrayTriplet;
