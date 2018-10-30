"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var LinkedNode_1 = require("../library/LinkedNode");
var LinkedListStack = /** @class */ (function () {
    function LinkedListStack() {
        this.head = null;
    }
    LinkedListStack.prototype.push = function (data) {
        var node = new LinkedNode_1.LinkedNode(data, this.head, null);
        this.head = node;
        return this.head;
    };
    LinkedListStack.prototype.pop = function () {
        if (!this.head) {
            return null;
        }
        var node = this.head;
        this.head = this.head.next;
        return node.data;
    };
    LinkedListStack.prototype.top = function () {
        if (!this.head) {
            return null;
        }
        return this.head.data;
    };
    return LinkedListStack;
}());
exports.LinkedListStack = LinkedListStack;
