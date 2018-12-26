var ListNode = /** @class */ (function () {
    function ListNode(val, next) {
        if (next === void 0) { next = null; }
        this.val = val;
        this.next = next;
    }
    return ListNode;
}());
//4->1->8->4->5
//5->0->1->8->4->5
//l1=5 l2=6 d=-1
//s1=0 s2=1
//p1=0 p2=1  h1=4 h2=0
//i=1     h1=1 h2=1
function findIntersection(l1, l2) {
    // find the length of both lists
    var head1 = l1;
    var head2 = l2;
    var startIndex1 = 0;
    var startIndex2 = 0;
    // subtract to get the difference
    var diff = getDiffLength(l1, l2);
    if (diff < 0) {
        startIndex2 = Math.abs(diff);
    }
    if (diff > 0) {
        startIndex1 = diff;
    }
    // move heads to the correct index
    var pointer1 = 0;
    var pointer2 = 0;
    while (pointer1 < startIndex1 || pointer2 < startIndex2) {
        if (pointer1 < startIndex1) {
            head1 = head1.next;
        }
        if (pointer2 < startIndex2) {
            head2 = head2.next;
        }
        pointer2++;
        pointer1++;
    }
    // find the intersection node
    var intersection = head1;
    while (head1 != null && head2 != null) {
        if (head1.val !== head2.val) {
            intersection = head1.next;
        }
        head1 = head1.next;
        head2 = head2.next;
    }
    return intersection;
}
function getDiffLength(l1, l2) {
    var length1 = 0;
    var length2 = 0;
    while (l1 != null || l2 != null) {
        if (l1 != null) {
            length1++;
            l1 = l1.next;
        }
        if (l2 != null) {
            length2++;
            l2 = l2.next;
        }
    }
    // subtract to get the difference
    return length1 - length2;
}
module.exports = {
    findIntersection: findIntersection, ListNode: ListNode
};
