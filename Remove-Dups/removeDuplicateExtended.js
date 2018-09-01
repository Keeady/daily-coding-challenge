"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function RemoveDuplicateExtended(linkedListNode) {
    var head = linkedListNode;
    var nextNodePointer;
    var prevNodePointer;
    //2  1 4 3 2 6
    while (linkedListNode) {
        nextNodePointer = linkedListNode.next;
        prevNodePointer = linkedListNode;
        while (nextNodePointer) {
            if (linkedListNode.data == nextNodePointer.data) {
                var next = nextNodePointer.next;
                nextNodePointer.next = null;
                prevNodePointer.next = next;
            }
            prevNodePointer = nextNodePointer;
            nextNodePointer = nextNodePointer.next;
        }
        linkedListNode = linkedListNode.next;
    }
    return head;
}
module.exports = RemoveDuplicateExtended;
