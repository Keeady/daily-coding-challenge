from Tree import move_tree_node


def test_move_up():
    five = move_tree_node.TreeNode(5)
    two = move_tree_node.TreeNode(2)
    five.left = two
    eight = move_tree_node.TreeNode(8)
    five.right = eight
    one = move_tree_node.TreeNode(1)
    three = move_tree_node.TreeNode(3)
    two.right = three
    two.left = one
    zero = move_tree_node.TreeNode(0)
    one.left = zero
    one_five = move_tree_node.TreeNode(1.5)
    one.right = one_five

    root = move_tree_node.move_node_up(five, two)
    assert root.val == 5
    assert root.right.val == eight.val
    assert root.left.val == 1
    assert one.left.val == 0
    assert one.right.val == 3
    assert zero.right.val == 1.5
    assert two.left is None
    assert two.right is None
