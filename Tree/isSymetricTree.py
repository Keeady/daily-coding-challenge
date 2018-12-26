class Solution:
    def isSymetricTree(self, root):
        return self.isMirror(root, root)

    def isSymetric(self, root):
        dictLevel = {}

        level = 0
        dictLevel = self.getLevel(root, level, dictLevel)

        for i in dictLevel:
            left = 0
            right = len(dictLevel[i]) - 1
            nodes = dictLevel[i]

            while left < right:
                if nodes[left] is None and nodes[right] is not None or nodes[right] is None and nodes[left] is not None:
                    return False

                if nodes[left] is not None and nodes[right] is not None and nodes[left].val != nodes[right].val:
                    return False

                left += 1
                right -= 1

        return True



    def getLevel(self, root, level, dictLevel):
        if not root:
            return dictLevel

        nodes = []
        if level in dictLevel:
            nodes = dictLevel.get(level)

        nodes.append(root.left)
        nodes.append(root.right)

        dictLevel[level] = nodes

        self.getLevel(root.left, level + 1, dictLevel)
        self.getLevel(root.right, level + 1, dictLevel)

        return dictLevel

    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:
            if root1.val != root2.val:
                return False

            return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)

        return False