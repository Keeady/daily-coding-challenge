import {TreeNode} from "./TreeNode";
import { binaryTreeToArray } from './binaryTreeToArray';
import {minHeapSort} from "../Heap-sort/min-heap-sort";
import {heapArrayToBinaryTree} from "./heapArrayToBinaryTree";

function binaryTreeToHeap(root: TreeNode) {
    let arr = binaryTreeToArray(root);
    arr.sort();
    arr = minHeapSort(arr);
    return heapArrayToBinaryTree(arr);
}

module.exports = binaryTreeToHeap;
