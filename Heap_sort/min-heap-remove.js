"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function minHeapRemove(arr) {
    arr[0] = arr.pop();
    var i = 0;
    while (i < arr.length) {
        var parent_1 = arr[i];
        var leftIndex = i * 2 + 1;
        var rightIndex = i * 2 + 2;
        var childIndex = void 0;
        if (rightIndex < arr.length) {
            //has 2 children
            if (arr[leftIndex] <= arr[rightIndex]) {
                childIndex = leftIndex;
            }
            else {
                childIndex = rightIndex;
            }
        }
        else if (leftIndex < arr.length) {
            childIndex = leftIndex;
        }
        else {
            // no children
            return arr;
        }
        if (parent_1 > arr[childIndex]) {
            //swap parent and child
            arr[i] = arr[childIndex];
            arr[childIndex] = parent_1;
        }
        else {
            return arr;
        }
        i++;
    }
    return arr;
}
exports.minHeapRemove = minHeapRemove;
module.exports = minHeapRemove;
