import {TreeNode} from "./TreeNode";

function findLowestCommonAncestors(root: TreeNode, node1: TreeNode, node2: TreeNode) {
    let path1 = [];
    let path2 = [];
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

    let index;
    let index2;
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

function search(root: TreeNode, node: TreeNode, list) {
    if (!root) {
        return null;
    }

    list.push(root);

    if (root.printValue() == node.printValue()) {
        return list;
    }

    if (node.printValue() < root.printValue()) {
        return search(root.getLeft(), node, list);
    } else if (node.printValue() > root.printValue()) {
        return search(root.getRight(), node, list);
    }
}

module.exports = findLowestCommonAncestors;
