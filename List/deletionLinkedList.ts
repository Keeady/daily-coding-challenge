import {LinkedNode} from "../library/LinkedNode";
import {LinkedList} from "../library/LinkedList";
export interface LinkedListInterface {
    deleteNode(node: LinkedNode): LinkedNode;
    insertAfter(node: LinkedNode, data: string): LinkedNode;
    getHead(): LinkedNode;
    getTail(): LinkedNode;
}
export class DeletionLinkedList extends LinkedList implements LinkedListInterface {
    protected head: LinkedNode;
    protected tail: LinkedNode;

    getHead() {
        return this.head;
    }

    getTail() {
        return this.tail;
    }

    add(data: string) {
        let node = super.add(data);
        this.tail = node;

        return node;
    }

    deleteNode(node: LinkedNode) {
        if (!node) {
            return this.head;
        }

        if (this.head == node) {
            this.head = this.head.next;
            if (this.tail == node) {
                this.tail = this.head;
            }
            return this.head;
        }

        let head = this.head;
        while (head != null) {
            if (head.next == node) {
                head.next = node.next;
                if (node == this.tail) {
                    this.tail = head;
                }
                node.next = null;
                node = null;
                return;
            }
            head = head.next;
        }

        return this.head;
    }

    insertAfter(node: LinkedNode, data: string) {
        const nextNode = new LinkedNode(data, null, null);
        if (!node) {
            this.head = nextNode;
            this.tail = nextNode;
            return nextNode;
        }

        if (node == this.tail) {
            this.tail = nextNode;
        }

        nextNode.next = node.next;
        node.next = nextNode;

        return nextNode;
    }
}
