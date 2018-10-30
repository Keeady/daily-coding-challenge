import {LinkedNode} from "./LinkedNode";

export class LinkedList {
    protected head: LinkedNode;

    getHead() {
        return this.head;
    }

    add(data: string) {
        let node = new LinkedNode(data, null, null);
        if (!this.head) {
            this.head = node;
            return this.head;
        }

        let lastNode = this.head;
        while (lastNode.next != null) {
            lastNode = lastNode.next;
        }

        lastNode.next = node;

        return node;
    }

    remove(data: string) {
        let currentNode = this.head;
        let prevNode = null;
        while(currentNode != null) {
            if (currentNode.data == data) {
                if (!prevNode) {
                    this.head = currentNode.next;
                    currentNode.next = null;
                } else {
                    prevNode.next = currentNode.next;
                }

                return currentNode;
            }

            prevNode = currentNode;
            currentNode = currentNode.next;
        }
    }
}
