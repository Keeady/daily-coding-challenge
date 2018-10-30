import {TreeNode} from "./TreeNode";

function postOrder(root: TreeNode, list: number[] = []) {
    if (root == null) {
        return;
    }

    postOrder(root.getRight(), list);
    postOrder(root.getLeft(), list);
    list.push(root.printValue());

    return list;
}

module.exports = postOrder;
