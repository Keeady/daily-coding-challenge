"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function postOrder(root, list) {
    if (list === void 0) { list = []; }
    if (root == null) {
        return;
    }
    postOrder(root.getRight(), list);
    postOrder(root.getLeft(), list);
    list.push(root.printValue());
    return list;
}
module.exports = postOrder;
