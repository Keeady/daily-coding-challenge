"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var LinkedNode = /** @class */ (function () {
    function LinkedNode(data, next, prev) {
        this.data = data;
        this.next = next;
        this.prev = prev;
    }
    return LinkedNode;
}());
exports.LinkedNode = LinkedNode;
