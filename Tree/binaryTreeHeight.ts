import {TreeNode} from "./TreeNode";

function findBinaryTreeHeight(root: TreeNode) {
    if (!root) {
        return 0;
    }

    return Math.max(findBinaryTreeHeight(root.getLeft()), findBinaryTreeHeight(root.getRight())) + 1;
}

module.exports = findBinaryTreeHeight;
