import {TreeNode} from "./TreeNode";

function preOrder(root: TreeNode, list: number[] = []) {
    if (root == null) {
        return;
    }
    list.push(root.printValue());
    preOrder(root.getLeft(), list);
    preOrder(root.getRight(), list);
    return list;
}

module.exports = preOrder;
