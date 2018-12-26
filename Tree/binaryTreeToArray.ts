import {TreeNode} from "./TreeNode";

export function binaryTreeToArray(root: TreeNode, arr = []) {
    if (root == null) {
        return;
    }
    arr.push(root.printValue());
    binaryTreeToArray(root.getLeft(), arr);
    binaryTreeToArray(root.getRight(), arr);
    return arr;
}

module.exports = binaryTreeToArray;
