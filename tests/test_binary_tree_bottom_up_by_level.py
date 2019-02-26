from Tree import print_binary_tree_bottom_up_by_level


def test_print():
    root = print_binary_tree_bottom_up_by_level.TreeNode(3)
    five = print_binary_tree_bottom_up_by_level.TreeNode(5)
    six = print_binary_tree_bottom_up_by_level.TreeNode(6)
    two = print_binary_tree_bottom_up_by_level.TreeNode(2)
    one = print_binary_tree_bottom_up_by_level.TreeNode(1)
    zero = print_binary_tree_bottom_up_by_level.TreeNode(0)
    eight = print_binary_tree_bottom_up_by_level.TreeNode(8)
    seven = print_binary_tree_bottom_up_by_level.TreeNode(7)
    four = print_binary_tree_bottom_up_by_level.TreeNode(4)
    root.left = five
    root.right = one
    five.left = six
    five.right = two
    one.left = zero
    one.right = eight
    two.left = seven
    two.right = four

    #[3, 5,1 ,6,2,0,8, 7,4]

    node_list = print_binary_tree_bottom_up_by_level.print(root)
    assert node_list == [[7,4], [6,2,0,8], [5,1], [3]]


def test_empty_tree():
    assert [] == print_binary_tree_bottom_up_by_level.print(None)


def test_single_node_tree():
    root = print_binary_tree_bottom_up_by_level.TreeNode(3)
    assert [[3]] == print_binary_tree_bottom_up_by_level.print(root)