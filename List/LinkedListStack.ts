import {LinkedNode} from "../library/LinkedNode";

export class LinkedListStack{
    protected head: LinkedNode = null;

    push(data: string) {
        const node = new LinkedNode(data, this.head, null);
        this.head = node;
        return this.head;
    }

    pop() {
        if (!this.head) {
            return null;
        }
        const node = this.head;
        this.head = this.head.next;
        return node.data;
    }

    top() {
        if (!this.head) {
            return null;
        }
        return this.head.data;
    }
}
