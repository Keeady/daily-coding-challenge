"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function preOrder(root) {
    var list = [];
    var stack = [];
    if (!root) {
        return list;
    }
    stack.push(root);
    var currentRoot;
    while (stack.length > 0) {
        currentRoot = stack.pop();
        list.push(currentRoot.printValue());
        if (currentRoot.getRight()) {
            stack.push(currentRoot.getRight());
        }
        if (currentRoot.getLeft()) {
            stack.push(currentRoot.getLeft());
        }
    }
    return list;
}
module.exports = preOrder;
