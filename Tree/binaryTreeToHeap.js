"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var binaryTreeToArray_1 = require("./binaryTreeToArray");
var min_heap_sort_1 = require("../Heap-sort/min-heap-sort");
var heapArrayToBinaryTree_1 = require("./heapArrayToBinaryTree");
function binaryTreeToHeap(root) {
    var arr = binaryTreeToArray_1.binaryTreeToArray(root);
    arr.sort();
    arr = min_heap_sort_1.minHeapSort(arr);
    return heapArrayToBinaryTree_1.heapArrayToBinaryTree(arr);
}
module.exports = binaryTreeToHeap;
