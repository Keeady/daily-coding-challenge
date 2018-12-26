def inorder(root, l = []):
    if not root:
        return l

    inorder(root.left, l)
    l.append(root.val)
    inorder(root.right, l)

    return l