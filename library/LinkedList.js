"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var LinkedNode_1 = require("./LinkedNode");
var LinkedList = /** @class */ (function () {
    function LinkedList() {
    }
    LinkedList.prototype.add = function (data) {
        var node = new LinkedNode_1.LinkedNode(data, null, null);
        if (!this.head) {
            this.head = node;
            return this.head;
        }
        var lastNode = this.head;
        while (lastNode.next != null) {
            lastNode = lastNode.next;
        }
        lastNode.next = node;
        return node;
    };
    LinkedList.prototype.remove = function (data) {
        var currentNode = this.head;
        var prevNode = null;
        while (currentNode != null) {
            if (currentNode.data == data) {
                if (!prevNode) {
                    this.head = currentNode.next;
                    currentNode.next = null;
                }
                else {
                    prevNode.next = currentNode.next;
                }
                return currentNode;
            }
            prevNode = currentNode;
            currentNode = currentNode.next;
        }
    };
    return LinkedList;
}());
exports.LinkedList = LinkedList;
