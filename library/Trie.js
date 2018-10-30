"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var TrieNode_1 = require("./TrieNode");
var Trie = /** @class */ (function () {
    function Trie() {
        this.root = new TrieNode_1.TrieNode('*');
    }
    Trie.prototype.getRoot = function () {
        return this.root;
    };
    Trie.prototype.add = function (word) {
        var chars = word.split('');
        var i;
        var node;
        var childNode;
        for (i = 0; i < chars.length; i++) {
            var char = chars[i];
            childNode = this.find(char, node);
            if (!childNode) {
                childNode = this.createChildNode(char, node);
            }
            node = childNode;
        }
    };
    Trie.prototype.find = function (char, node) {
        if (node === void 0) { node = this.root; }
        if (node.has(char)) {
            return node.get(char);
        }
        return null;
    };
    Trie.prototype.createChildNode = function (char, node) {
        if (node === void 0) { node = this.root; }
        var childNode = new TrieNode_1.TrieNode(char);
        node.add(char, childNode);
        return childNode;
    };
    return Trie;
}());
exports.Trie = Trie;
