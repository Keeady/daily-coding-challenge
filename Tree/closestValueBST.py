from math import fabs

class Solution:
    def findClosestValue(self, root, target):
        temp = fabs(target - root.val)
        return self.search(root, target, temp)

    def search(self, root, target, temp):
        if root is None:
            return temp

        if target == root.val:
            return root.val

        if fabs(target - root.val) < fabs(temp - target):
            temp = root.val

        if target < root.val:
            return self.search(root.left, target, temp)

        else:
            return self.search(root.right, target, temp)

