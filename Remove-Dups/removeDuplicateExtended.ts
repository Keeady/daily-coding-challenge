import LinkedNode from "../library/LinkedNode";

function RemoveDuplicateExtended(linkedListNode: LinkedNode) {
    let head = linkedListNode;
    let nextNodePointer;
    let prevNodePointer;
//2  1 4 3 2 6
    while (linkedListNode) {
        nextNodePointer = linkedListNode.next;
        prevNodePointer = linkedListNode;
        while (nextNodePointer) {
            if (linkedListNode.data == nextNodePointer.data) {
                let next = nextNodePointer.next;
                nextNodePointer.next = null;
                prevNodePointer.next  = next;
            }

            prevNodePointer = nextNodePointer;
            nextNodePointer = nextNodePointer.next;
        }

        linkedListNode = linkedListNode.next;
    }

    return head;
}

module.exports = RemoveDuplicateExtended;
