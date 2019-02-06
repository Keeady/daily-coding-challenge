"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function minHeapInsert(arr, value) {
    arr.push(value);
    if (arr.length === 1) {
        return arr;
    }
    var i = arr.length - 1;
    while (i > 0) {
        var parentIndex = parseInt(Number((i - 1) / 2).toString());
        var parent_1 = arr[parentIndex];
        if (parent_1 > value) {
            arr[parentIndex] = value;
            arr[i] = parent_1;
            i = parentIndex;
        }
        else {
            return i;
        }
    }
    return i;
}
exports.minHeapInsert = minHeapInsert;
module.exports = minHeapInsert;
