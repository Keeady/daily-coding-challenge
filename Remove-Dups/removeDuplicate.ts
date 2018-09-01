import LinkedNode from "../library/LinkedNode";

function RemoveDuplicate(linkedListNode: LinkedNode) {
    let head = linkedListNode;
    let list = new Map();
    list.set(linkedListNode.data, true);

    while (linkedListNode && linkedListNode.next) {
        if (list.has(linkedListNode.next.data)) {
            let next = linkedListNode.next.next;
            linkedListNode.next.next = null;
            linkedListNode.next  = next;
        } else {
            list.set(linkedListNode.next.data, true);
        }

        linkedListNode = linkedListNode.next;
    }

    return head;
}

module.exports = RemoveDuplicate;
