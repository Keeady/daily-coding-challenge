from Tree import smallest_subtree_with_all_deepest_nodes


def test_find_max_level():
    root = smallest_subtree_with_all_deepest_nodes.TreeNode(3)
    five = smallest_subtree_with_all_deepest_nodes.TreeNode(5)
    six = smallest_subtree_with_all_deepest_nodes.TreeNode(6)
    two = smallest_subtree_with_all_deepest_nodes.TreeNode(2)
    one = smallest_subtree_with_all_deepest_nodes.TreeNode(1)
    zero = smallest_subtree_with_all_deepest_nodes.TreeNode(0)
    eight = smallest_subtree_with_all_deepest_nodes.TreeNode(8)
    seven = smallest_subtree_with_all_deepest_nodes.TreeNode(7)
    four = smallest_subtree_with_all_deepest_nodes.TreeNode(4)
    root.left = five
    root.right = one
    five.left = six
    five.right = two
    one.left = zero
    one.right = eight
    two.left = seven
    two.right = four


    assert 4 == smallest_subtree_with_all_deepest_nodes.find_max_level(root)

    assert 4 == smallest_subtree_with_all_deepest_nodes.find_max_level_subtree(root, {})

    node = smallest_subtree_with_all_deepest_nodes.find_max_subtree(root, {})
    assert node.val == 2

    nine = smallest_subtree_with_all_deepest_nodes.TreeNode(9)
    six.right = nine

    node = smallest_subtree_with_all_deepest_nodes.find_max_subtree(root, {})
    assert node.val == 5

    ten = smallest_subtree_with_all_deepest_nodes.TreeNode(10)
    eight.right = ten

    node = smallest_subtree_with_all_deepest_nodes.find_max_subtree(root, {})
    assert node.val == 3


def test_find_max_level_no_space():
    root = smallest_subtree_with_all_deepest_nodes.TreeNode(3)
    five = smallest_subtree_with_all_deepest_nodes.TreeNode(5)
    six = smallest_subtree_with_all_deepest_nodes.TreeNode(6)
    two = smallest_subtree_with_all_deepest_nodes.TreeNode(2)
    one = smallest_subtree_with_all_deepest_nodes.TreeNode(1)
    zero = smallest_subtree_with_all_deepest_nodes.TreeNode(0)
    eight = smallest_subtree_with_all_deepest_nodes.TreeNode(8)
    seven = smallest_subtree_with_all_deepest_nodes.TreeNode(7)
    four = smallest_subtree_with_all_deepest_nodes.TreeNode(4)
    root.left = five
    root.right = one
    five.left = six
    five.right = two
    one.left = zero
    one.right = eight
    two.left = seven
    two.right = four

    node = smallest_subtree_with_all_deepest_nodes.find_max_subtree_no_extra_space(root)
    assert node.val == 2

    nine = smallest_subtree_with_all_deepest_nodes.TreeNode(9)
    six.right = nine

    node = smallest_subtree_with_all_deepest_nodes.find_max_subtree_no_extra_space(root)
    assert node.val == 5

    ten = smallest_subtree_with_all_deepest_nodes.TreeNode(10)
    eight.right = ten

    node = smallest_subtree_with_all_deepest_nodes.find_max_subtree_no_extra_space(root)
    assert node.val == 3


def test_find_deepest_node():
    root = smallest_subtree_with_all_deepest_nodes.TreeNode(3)
    five = smallest_subtree_with_all_deepest_nodes.TreeNode(5)
    six = smallest_subtree_with_all_deepest_nodes.TreeNode(6)
    two = smallest_subtree_with_all_deepest_nodes.TreeNode(2)
    one = smallest_subtree_with_all_deepest_nodes.TreeNode(1)
    zero = smallest_subtree_with_all_deepest_nodes.TreeNode(0)
    eight = smallest_subtree_with_all_deepest_nodes.TreeNode(8)
    seven = smallest_subtree_with_all_deepest_nodes.TreeNode(7)
    four = smallest_subtree_with_all_deepest_nodes.TreeNode(4)
    root.left = five
    root.right = one
    five.left = six
    five.right = two
    one.left = zero
    one.right = eight
    two.left = seven
    two.right = four

    node = smallest_subtree_with_all_deepest_nodes.find_deepest_node_bfs(root)
    assert node.val == 4

    nine = smallest_subtree_with_all_deepest_nodes.TreeNode(9)
    six.right = nine

    node = smallest_subtree_with_all_deepest_nodes.find_deepest_node_bfs(root)
    assert node.val == 4

    ten = smallest_subtree_with_all_deepest_nodes.TreeNode(10)
    eight.right = ten

    node = smallest_subtree_with_all_deepest_nodes.find_deepest_node_bfs(root)
    assert node.val == 10
