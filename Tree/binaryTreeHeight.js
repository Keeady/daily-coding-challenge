"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function findBinaryTreeHeight(root) {
    if (!root) {
        return 0;
    }
    return Math.max(findBinaryTreeHeight(root.getLeft()), findBinaryTreeHeight(root.getRight())) + 1;
}
module.exports = findBinaryTreeHeight;
