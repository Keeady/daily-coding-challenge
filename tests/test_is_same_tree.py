from Tree import same_tree


def test_is_same():
    assert True == same_tree.is_same_tree(None, None)

    assert False == same_tree.is_same_tree(None, same_tree.TreeNode(1))

    assert True == same_tree.is_same_tree(same_tree.TreeNode(1), same_tree.TreeNode(1))

    one = same_tree.TreeNode(1)
    two = same_tree.TreeNode(2)
    three = same_tree.TreeNode(3)
    one.left = two
    one.right = three

    one2 = same_tree.TreeNode(1)
    two2 = same_tree.TreeNode(2)
    three2 = same_tree.TreeNode(3)
    one2.left = two2
    one2.right = three2

    assert True == same_tree.is_same_tree(one, one2)

    one = same_tree.TreeNode(1)
    two = same_tree.TreeNode(2)
    three = same_tree.TreeNode(4)
    one.left = two
    one.right = three

    one2 = same_tree.TreeNode(1)
    two2 = same_tree.TreeNode(2)
    three2 = same_tree.TreeNode(3)
    one2.left = two2
    one2.right = three2

    assert False == same_tree.is_same_tree(one, one2)


    one = same_tree.TreeNode(1)
    two = same_tree.TreeNode(2)
    one.left = two
    one.right = three

    one2 = same_tree.TreeNode(1)
    two2 = same_tree.TreeNode(2)
    three2 = same_tree.TreeNode(3)
    one2.left = two2
    one2.right = three2

    assert False == same_tree.is_same_tree(one, one2)


    one = same_tree.TreeNode(1)
    two = same_tree.TreeNode(2)
    three = same_tree.TreeNode(4)
    one.left = two
    one.right = three

    one2 = same_tree.TreeNode(1)
    two2 = same_tree.TreeNode(2)
    one2.left = two2
    one2.right = three2

    assert False == same_tree.is_same_tree(one, one2)