"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function preOrder(root, list) {
    if (list === void 0) { list = []; }
    if (root == null) {
        return;
    }
    list.push(root.printValue());
    preOrder(root.getLeft(), list);
    preOrder(root.getRight(), list);
    return list;
}
module.exports = preOrder;
