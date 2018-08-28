export class LinkedNode {
    data: string;
    next: LinkedNode;
    prev: LinkedNode;

    constructor(data, next, prev) {
        this.data = data;
        this.next = next;
        this.prev = prev;
    }
}
