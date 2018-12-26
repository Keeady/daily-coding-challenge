import sys

class Solution:
    def isValidBST(self, root):
        if not root:
            return True

        return self.isValidSubTree(root, -sys.maxsize -1, sys.maxsize)

    def isValidSubTree(self, root, min, max):
        if root is None:
            return True

        if root.val > min and root.val < max:
            return self.isValidSubTree(root.left, min, root.val) and self.isValidSubTree(root.right, root.val, max)
        else:
            return False

# left child > parent's min and < parent.val
# right child > parent.val and < max from parent

#