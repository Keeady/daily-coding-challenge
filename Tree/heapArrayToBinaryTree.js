"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var TreeNode_1 = require("./TreeNode");
function heapArrayToBinaryTree(arr) {
    var i = 0;
    var root = new TreeNode_1.TreeNode(arr[i]);
    toBinaryTree(arr, root, i);
    return root;
}
exports.heapArrayToBinaryTree = heapArrayToBinaryTree;
function toBinaryTree(arr, node, i) {
    if (i * 2 + 1 >= arr.length && i * 2 + 2 >= arr.length) {
        return;
    }
    if (i * 2 + 1 < arr.length) {
        var left = new TreeNode_1.TreeNode(arr[i * 2 + 1]);
        node.setLeft(left);
        toBinaryTree(arr, left, i * 2 + 1);
    }
    if (i * 2 + 2 < arr.length) {
        var right = new TreeNode_1.TreeNode(arr[i * 2 + 2]);
        node.setRight(right);
        toBinaryTree(arr, right, i * 2 + 2);
    }
}
module.exports = heapArrayToBinaryTree;
