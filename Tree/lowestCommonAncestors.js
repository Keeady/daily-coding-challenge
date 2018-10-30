"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function findLowestCommonAncestors(root, node1, node2) {
    var path1 = [];
    var path2 = [];
    if (!root) {
        return null;
    }
    path1 = search(root, node1, path1);
    if (path1 == null) {
        return null;
    }
    path2 = search(root, node2, path2);
    if (path2 == null) {
        return null;
    }
    var index;
    var index2;
    for (index = path1.length - 1; index >= 0; index--) {
        index2 = path2.length - 1;
        while (index2 >= 0) {
            if (path1[index] == path2[index2]) {
                return path1[index];
            }
            index2--;
        }
    }
    return null;
}
function search(root, node, list) {
    if (!root) {
        return null;
    }
    list.push(root);
    if (root.printValue() == node.printValue()) {
        return list;
    }
    if (node.printValue() < root.printValue()) {
        return search(root.getLeft(), node, list);
    }
    else if (node.printValue() > root.printValue()) {
        return search(root.getRight(), node, list);
    }
}
module.exports = findLowestCommonAncestors;
