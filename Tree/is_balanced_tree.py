class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_balanced_tree(root):
    return check_balance(root) != -1


def check_balance(root: TreeNode):
    if not root:
        return 0

    left = check_balance(root.left)
    right = check_balance(root.right)

    if left == -1 or right == -1 or abs(left - right) > 1:
        return -1

    max_height = max(left, right) + 1

    return max_height

