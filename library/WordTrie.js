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
var Trie_1 = require("./Trie");
var WordTrie = /** @class */ (function (_super) {
    __extends(WordTrie, _super);
    function WordTrie() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    /**
     * @param chars
     */
    WordTrie.prototype.addChars = function (chars) {
        var i;
        var node = this.getRoot();
        for (i = 0; i < chars.length; i++) {
            var childNode = this.find(chars[i], node);
            if (!childNode) {
                childNode = this.createChildNode(chars[i], node);
            }
            node = childNode;
        }
    };
    WordTrie.prototype.findChars = function (chars) {
        var i;
        var node = this.getRoot();
        for (i = 0; i < chars.length; i++) {
            node = this.find(chars[i], node);
            if (!node) {
                return false;
            }
        }
        return true;
    };
    return WordTrie;
}(Trie_1.Trie));
exports.WordTrie = WordTrie;
