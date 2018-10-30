import {LinkedNode} from "../library/LinkedNode";

//5->3->2->3
function isListCycle(head: LinkedNode): boolean {
    //empty list: no cycle
    if (!head) {
        return false;
    }

    //Visited nodes
    let visiteNodes = new Map<LinkedNode, boolean>();

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
