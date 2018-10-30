import {TrieNode} from "./TrieNode";

export class Trie {
    protected root: TrieNode;

    constructor() {
        this.root = new TrieNode('*');
    }

    getRoot() {
        return this.root;
    }

    add(word: string) {
        let chars = word.split('');
        let i;
        let node: TrieNode;
        let childNode: TrieNode;
        for (i = 0; i < chars.length; i++) {
            let char = chars[i];
            childNode = this.find(char, node);
            if (!childNode) {
                childNode = this.createChildNode(char, node);
            }

            node = childNode;
        }
    }

    find(char: string, node: TrieNode = this.root) {
        if (node.has(char)) {
            return node.get(char);
        }

        return null;
    }

    createChildNode(char, node: TrieNode = this.root) {
        let childNode = new TrieNode(char);
        node.add(char, childNode);

        return childNode;
    }
}
