import {Trie} from "./Trie";

export class WordTrie extends Trie {
    /**
     * @param chars
     */
    addChars(chars) {
        let i;
        let node = this.getRoot();

        for (i = 0; i < chars.length; i++) {
            let childNode = this.find(chars[i], node);
            if (!childNode) {
                childNode = this.createChildNode(chars[i], node);
            }

            node = childNode;
        }
    }

    findChars(chars) {
        let i;
        let node = this.getRoot();
        for (i = 0; i < chars.length; i++) {
            node = this.find(chars[i], node);
            if (!node) {
                return false;
            }
        }

        return true;
    }
}
