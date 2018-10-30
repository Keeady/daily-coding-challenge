"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var TreeNode = /** @class */ (function () {
    function TreeNode(data, left, right) {
        if (left === void 0) { left = null; }
        if (right === void 0) { right = null; }
        this.data = data;
        this.left = left;
        this.right = right;
    }
    TreeNode.prototype.printValue = function () {
        return this.data;
    };
    TreeNode.prototype.getLeft = function () {
        return this.left;
    };
    TreeNode.prototype.setLeft = function (node) {
        this.left = node;
    };
    TreeNode.prototype.getRight = function () {
        return this.right;
    };
    TreeNode.prototype.setRight = function (node) {
        this.right = node;
    };
    return TreeNode;
}());
exports.TreeNode = TreeNode;
