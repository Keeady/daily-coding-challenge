class Solution:
    def sumRootToLeaf(self, root):
        if not root:
            return 0

        return self.sumPath(root, 0)

    def sumPath(self, root, sum):
        if not root:
            return 0

        sum = sum * 10 + root.val

        if not root.left and not root.right:
            return sum

        sum = self.sumPath(root.left, sum) + self.sumPath(root.right, sum)

        return sum

