"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function findLowestCommonAncestors(root, node1, node2) {
    var path1 = [];
    if (!root) {
        return null;
    }
    path1 = search(root, node1, node2, path1);
    if (path1 == null) {
        return null;
    }
    return path1;
}
function search(root, node1, node2, list) {
    if (!root) {
        return [];
    }
    if (root.printValue() == node1.printValue() || root.printValue() == node2.printValue()) {
        return list.pop();
    }
    list.push(root);
    if (root.printValue() > node1.printValue() && root.printValue() < node2.printValue() ||
        root.printValue() > node2.printValue() && root.printValue() < node1.printValue()) {
        return root;
    }
    if (root.printValue() > node1.printValue() && root.printValue() > node2.printValue()) {
        return search(root.getLeft(), node1, node2, list);
    }
    if (root.printValue() < node1.printValue() && root.printValue() < node2.printValue()) {
        return search(root.getRight(), node1, node2, list);
    }
    return list.pop();
}
module.exports = findLowestCommonAncestors;
