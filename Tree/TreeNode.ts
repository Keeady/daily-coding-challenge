export class TreeNode {
    protected data: number;
    protected left: TreeNode;
    protected right: TreeNode;

    constructor(data: number, left: TreeNode = null, right: TreeNode = null) {
        this.data = data;
        this.left = left;
        this.right = right;
    }

    public printValue() {
        return this.data;
    }

    public getLeft() {
        return this.left;
    }

    public setLeft(node: TreeNode) {
        this.left = node;
    }

    public getRight() {
        return this.right;
    }

    public setRight(node: TreeNode) {
        this.right = node;
    }
}
