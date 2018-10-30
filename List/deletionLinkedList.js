"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var LinkedNode_1 = require("../library/LinkedNode");
var LinkedList_1 = require("../library/LinkedList");
var DeletionLinkedList = /** @class */ (function (_super) {
    __extends(DeletionLinkedList, _super);
    function DeletionLinkedList() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    DeletionLinkedList.prototype.getHead = function () {
        return this.head;
    };
    DeletionLinkedList.prototype.getTail = function () {
        return this.tail;
    };
    DeletionLinkedList.prototype.add = function (data) {
        var node = _super.prototype.add.call(this, data);
        this.tail = node;
        return node;
    };
    DeletionLinkedList.prototype.deleteNode = function (node) {
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
        var head = this.head;
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
    };
    DeletionLinkedList.prototype.insertAfter = function (node, data) {
        var nextNode = new LinkedNode_1.LinkedNode(data, null, null);
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
    };
    return DeletionLinkedList;
}(LinkedList_1.LinkedList));
exports.DeletionLinkedList = DeletionLinkedList;
