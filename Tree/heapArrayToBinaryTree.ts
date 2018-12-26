import {TreeNode} from "./TreeNode";

export function heapArrayToBinaryTree(arr) {
    let i = 0;
    let root = new TreeNode(arr[i]);

    toBinaryTree(arr, root, i);

    return root;
}

function toBinaryTree(arr, node, i) {
    if (i * 2 + 1 >= arr.length && i * 2 + 2 >= arr.length) {
        return;
    }

    if (i * 2 + 1 < arr.length) {
        let left = new TreeNode(arr[i * 2 + 1]);
        node.setLeft(left);
        toBinaryTree(arr, left, i * 2 + 1);
    }

    if (i * 2 + 2 < arr.length) {
        let right = new TreeNode(arr[i * 2 + 2]);
        node.setRight(right);
        toBinaryTree(arr, right, i * 2 + 2);
    }
}

module.exports = heapArrayToBinaryTree;
