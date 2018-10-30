export class TrieNode {
    protected children: Map<string, TrieNode>;
    protected value: string;

    constructor(value: string) {
        this.value = value;
        this.children = new Map<string, TrieNode>();
    }

    getValue() {
        return this.value;
    }

    getChildren() {
        return this.children;
    }

    has(char: string) {
        return this.children.has(char);
    }

    get(char: string) {
        return this.children.get(char);
    }

    add(char: string, node: TrieNode) {
        this.children.set(char, node);
    }
}
