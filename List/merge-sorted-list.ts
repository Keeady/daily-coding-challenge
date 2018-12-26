import {LinkedNode} from "../library/LinkedNode";

function mergeSortedList(l1: LinkedNode, l2: LinkedNode) {
    // merge each node in new list
    let head;
    let prev;
    let temp;
    while (l1 != null && l2 != null) {
        if (l1.data <= l2.data) {
            temp = l1;
            l1 = l1.next;
        } else {
            temp = l2;
            l2 = l2.next;
        }

        if (!head) {
            head = temp;
        } else {
            prev.next = temp;
        }

        prev = temp;
    }

    if (l1 !== null) {
        prev.next = l1;
    }

    if (l2 !== null) {
        prev.next = l2;
    }

    return head;
}
