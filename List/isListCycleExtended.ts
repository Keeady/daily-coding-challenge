import {LinkedNode} from "../library/LinkedNode";

function isListCycle(head: LinkedNode) {
    if (!head) {
        return false;
    }

    let left = head;
    let right = head.next;
    while (right != null) {
        if (right == left || right.next == left) {
            return true;
        }

        if (!right || !right.next || !right.next.next) {
            return false;
        }

        right = right.next.next;
        left = left.next;
    }

    return false;
}

module.exports = isListCycle;
