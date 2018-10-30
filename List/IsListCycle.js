"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
//5->3->2->3
function isListCycle(head) {
    //empty list: no cycle
    if (!head) {
        return false;
    }
    //Visited nodes
    var visiteNodes = new Map();
    //iterate to the end of the list or until cycle is found
    while (head != null) {
        //cycle found: node pointing to a node that has been visited before
        if (visiteNodes.has(head.next)) {
            return true;
        }
        //add visited nodes to list
        visiteNodes.set(head, true);
        //moving to the next node
        head = head.next;
    }
    return false;
}
module.exports = isListCycle;
