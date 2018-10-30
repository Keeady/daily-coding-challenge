"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var TrieNode = /** @class */ (function () {
    function TrieNode(value) {
        this.value = value;
        this.children = new Map();
    }
    TrieNode.prototype.getValue = function () {
        return this.value;
    };
    TrieNode.prototype.getChildren = function () {
        return this.children;
    };
    TrieNode.prototype.has = function (char) {
        return this.children.has(char);
    };
    TrieNode.prototype.get = function (char) {
        return this.children.get(char);
    };
    TrieNode.prototype.add = function (char, node) {
        this.children.set(char, node);
    };
    return TrieNode;
}());
exports.TrieNode = TrieNode;
