class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def path_sum(root: TreeNode):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val

    sum = root.val
    left = float('-inf')
    right = float('-inf')
    if root.left:
        left = path_sum(root.left)

    if root.right:
        right = path_sum(root.right)

    return max(sum, left, right, left + right + sum, left + sum, right + sum)
