"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function minHeapSort(arr) {
    var i = arr.length - 1;
    while (i > 0) {
        var element = arr[i];
        var parentIndex = parseInt(Number((i - 1) / 2).toString());
        var parent_1 = arr[parentIndex];
        if (parent_1 > element) {
            arr[parentIndex] = element;
            arr[i] = parent_1;
            var leftIndex = i * 2 + 1;
            var rightIndex = i * 2 + 2;
            if (leftIndex < arr.length && arr[i] > arr[leftIndex] || rightIndex < arr.length && arr[i] > arr[rightIndex]) {
                i = rightIndex + 1;
            }
        }
        i--;
    }
    return arr;
}
exports.minHeapSort = minHeapSort;
module.exports = minHeapSort;
