import {LinkedNode} from "../library/LinkedNode";

function findMthElement(node: LinkedNode, m: number) {
    if (!node) {
        return null;
    }

    let leftPointer = node;
    let rightPointer = node;

    rightPointer = moveMSteps(rightPointer, m);
    while (rightPointer != null) {
        rightPointer = rightPointer.next;
        leftPointer = leftPointer.next;
    }

    return leftPointer;
}

function moveMSteps(rightPointer: LinkedNode, m: number) {
    let index = 0;
    while (index <= m && rightPointer != null) {
        rightPointer = rightPointer.next;
        index++;
    }

    return rightPointer;
}

module.exports = findMthElement;
