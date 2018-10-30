"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function findMthElement(node, m) {
    if (!node) {
        return null;
    }
    var leftPointer = node;
    var rightPointer = node;
    rightPointer = moveMSteps(rightPointer, m);
    while (rightPointer != null) {
        rightPointer = rightPointer.next;
        leftPointer = leftPointer.next;
    }
    return leftPointer;
}
function moveMSteps(rightPointer, m) {
    var index = 0;
    while (index <= m && rightPointer != null) {
        rightPointer = rightPointer.next;
        index++;
    }
    return rightPointer;
}
module.exports = findMthElement;
