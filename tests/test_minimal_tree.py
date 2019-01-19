from Tree import minimal_tree


def test_min_tree():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    root = minimal_tree.minimal_tree(arr)
    assert root.data == 4
    assert root.left.data == 2
    assert root.right.data == 6
    assert root.left.left.data == 1
    assert root.left.right.data == 3
    assert root.right.left.data == 5
    assert root.right.right.data == 7
    assert root.right.right.left is None
    assert root.right.right.right.data == 8

def test_min_empty_tree():
    arr = []

    root = minimal_tree.minimal_tree(arr)
    assert root is None

def test_min_root_tree():
    arr = [4]
    root = minimal_tree.minimal_tree(arr)
    assert root.data == 4
    assert root.left is None
    assert root.right is None


def test_min_leaf_tree():
    arr = [4, 5]
    root = minimal_tree.minimal_tree(arr)
    assert root.data == 4
    assert root.left is None
    assert root.right.data == 5
