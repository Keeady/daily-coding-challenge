class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def delete(root: TreeNode, val):
    if not root:
        return None

    [parent, node] = find_node_bst(None, root, val)

    if not node:
        return root

    if node.val == root.val:
        root = delete_root_bst(node)
    else:
        delete_node_bst(parent, node)

    node.left = None
    node.right = None

    return root


def find_node_bst(parent: TreeNode, root: TreeNode, val):
    if not root:
        return [parent, None]

    if root.val == val:
        return [parent, root]

    if val < root.val:
        # left
        return find_node_bst(root, root.left, val)

    elif val > root.val:
        # right
        return find_node_bst(root, root.right, val)

    return [parent, None]


def delete_node_bst(parent, node):
    #case leaf: remove reference from parent node
    #case has left or/and right: move one child up to be referenced by parent node
    new_child = None

    if node.left and node.right:
        return move_node_up(parent, node)
    if node.right:
        new_child = node.right
    else:
        new_child = node.left

    if parent.val < node.val:
        parent.right = new_child
    else:
        parent.left = new_child
    return new_child


def delete_root_bst(root: TreeNode):
    #case root node: move one child up
    if not root.left and not root.right:
        return None

    if root.right:
        [parent, new_root] = find_new_root_left_child(root, root.right)
        parent.left = new_root.right
        new_root.right = root.right
        new_root.left = root.left
    else:
        new_root = root.left

    return new_root

def find_new_root_left_child(parent, root):
    if not root.left:
        return [parent, root]

    if root.left:
        return find_new_root_left_child(root, root.left)


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