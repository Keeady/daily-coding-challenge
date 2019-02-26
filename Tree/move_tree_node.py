class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def move_node_up(parent, node):
    left_child = node.left
    right_child = left_child.right
    parent.left = left_child
    left_child.right = node.right

    node.left = None
    node.right = None

    switch(left_child.left, right_child)

    return parent

def switch(parent, right):
    if right is None:
        return parent

    right_child = parent.right
    parent.right = right

    return switch(parent.left, right_child)
