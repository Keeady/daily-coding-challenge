"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function isListCycle(head) {
    if (!head) {
        return false;
    }
    var left = head;
    var right = head.next;
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
