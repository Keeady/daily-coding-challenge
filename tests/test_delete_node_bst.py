from Tree import delete_node_bst


def test_delete_bst():
    five = delete_node_bst.TreeNode(5)
    two = delete_node_bst.TreeNode(2)
    five.left = two
    three = delete_node_bst.TreeNode(3)
    two.right = three
    four = delete_node_bst.TreeNode(4)
    two.left = four

    root = delete_node_bst.delete(five, 5)
    assert root.val == 2


def test_delete_root_bst():
    five = delete_node_bst.TreeNode(5)
    two = delete_node_bst.TreeNode(2)
    eight = delete_node_bst.TreeNode(8)
    five.left = two
    five.right = eight
    three = delete_node_bst.TreeNode(3)
    two.right = three
    four = delete_node_bst.TreeNode(4)
    two.left = four

    nine = delete_node_bst.TreeNode(9)
    eight.right = nine
    six = delete_node_bst.TreeNode(6)
    eight.left = six
    seven = delete_node_bst.TreeNode(7)
    six.right = seven

    root = delete_node_bst.delete(five, 5)
    assert root.val == 6
    assert eight.left.val == 7
    assert root.right == eight


def test_delete_leaf():
    five = delete_node_bst.TreeNode(5)
    two = delete_node_bst.TreeNode(2)
    eight = delete_node_bst.TreeNode(8)
    five.left = two
    five.right = eight
    three = delete_node_bst.TreeNode(3)
    two.right = three
    one = delete_node_bst.TreeNode(1)
    two.left = one

    nine = delete_node_bst.TreeNode(9)
    eight.right = nine
    six = delete_node_bst.TreeNode(6)
    eight.left = six
    seven = delete_node_bst.TreeNode(7)
    six.right = seven

    root = delete_node_bst.delete(five, 4)
    assert root.val == 5

    root = delete_node_bst.delete(five, 1)
    assert root.val == 5
    assert two.left is None

    root = delete_node_bst.delete(five, 9)
    assert root.val == 5
    assert eight.right is None

    root = delete_node_bst.delete(five, 3)
    assert root.val == 5
    assert two.right is None


def test_delete_parent_node():
    five = delete_node_bst.TreeNode(5)
    two = delete_node_bst.TreeNode(2)
    eight = delete_node_bst.TreeNode(8)
    five.left = two
    five.right = eight
    three = delete_node_bst.TreeNode(3)
    two.right = three
    one = delete_node_bst.TreeNode(1)
    two.left = one

    nine = delete_node_bst.TreeNode(9)
    eight.right = nine
    six = delete_node_bst.TreeNode(6)
    eight.left = six
    seven = delete_node_bst.TreeNode(7)
    six.right = seven

    root = delete_node_bst.delete(five, 6)
    assert root.val == 5
    assert eight.left == seven

    root = delete_node_bst.delete(five, 2)
    assert root.val == 5
    assert root.left == one
    assert one.right == three

    root = delete_node_bst.delete(five, 8)
    assert root.val == 5
    assert root.left.val == seven.val
    assert seven.right.val == nine.val


def test_delete():
    one = delete_node_bst.TreeNode(1)
    two = delete_node_bst.TreeNode(2)
    one.right = two
    root = delete_node_bst.delete(one, 1)
    assert root.val == 2