"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function mergeSortedList(l1, l2) {
    // merge each node in new list
    var head;
    var prev;
    var temp;
    while (l1 != null && l2 != null) {
        if (l1.data <= l2.data) {
            temp = l1;
            l1 = l1.next;
        }
        else {
            temp = l2;
            l2 = l2.next;
        }
        if (!head) {
            head = temp;
        }
        else {
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
