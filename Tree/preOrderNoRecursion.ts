import {TreeNode} from "./TreeNode";

function preOrder(root: TreeNode) {
    let list: number[] = [];
    let stack = [];
    if (!root) {
        return list;
    }

    stack.push(root);
    let currentRoot;

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
