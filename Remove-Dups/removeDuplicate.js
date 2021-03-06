"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function RemoveDuplicate(linkedListNode) {
    var head = linkedListNode;
    var list = new Map();
    list.set(linkedListNode.data, true);
    while (linkedListNode && linkedListNode.next) {
        if (list.has(linkedListNode.next.data)) {
            var next = linkedListNode.next.next;
            linkedListNode.next.next = null;
            linkedListNode.next = next;
        }
        else {
            list.set(linkedListNode.next.data, true);
        }
        linkedListNode = linkedListNode.next;
    }
    return head;
}
module.exports = RemoveDuplicate;
