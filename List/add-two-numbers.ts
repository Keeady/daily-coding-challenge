import {LinkedNode} from "../library/LinkedNode";

/**
 * @param {LinkedNode} l1
 * @param {LinkedNode} l2
 * @return {LinkedNode}
 */
function addTwoNumbers (l1: LinkedNode, l2: LinkedNode) {
    let carry = 0;
    let sum = 0; //sum at each iteration
    let val1, val2; //corresponding value of l1, l2
    let output; // head of linkedlist of output
    let prev;
    let temp;

    while (l1 != null || l2 != null) {
        val1 = l1 ? l1.data : 0;
        val2 = l2 ? l2.data : 0;

        sum = carry + parseInt(val1) + parseInt(val2);
        carry = 0;
        if (sum >= 10) {
            carry = 1;
            sum -= 10;
        }

        temp = new LinkedNode(sum);
        //pointer to head;
        if (!output) {
            output = temp;
        } else {
            prev.next = temp;
        }

        prev = temp;
        //console.log(node);
        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;
    }

    if (carry > 0) {
        prev.next = new LinkedNode(carry);
    }

    return output;
}

module.exports = addTwoNumbers;
