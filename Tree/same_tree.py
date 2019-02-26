class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True

    if not root1 or not root2 or root1.val != root2.val:
        return False

    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)