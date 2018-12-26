"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function binaryTreeToArray(root, arr) {
    if (arr === void 0) { arr = []; }
    if (root == null) {
        return;
    }
    arr.push(root.printValue());
    binaryTreeToArray(root.getLeft(), arr);
    binaryTreeToArray(root.getRight(), arr);
    return arr;
}
exports.binaryTreeToArray = binaryTreeToArray;
module.exports = binaryTreeToArray;
