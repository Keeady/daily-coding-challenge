from Tree import is_balanced_tree

def test_bad_balance():
    one = is_balanced_tree.TreeNode(1)
    two = is_balanced_tree.TreeNode(2)
    three = is_balanced_tree.TreeNode(3)
    one.left = two
    two.left = three

    assert False == is_balanced_tree.is_balanced_tree(one)

def test_bad_balances():
    one = is_balanced_tree.TreeNode(1)
    two = is_balanced_tree.TreeNode(2)
    three = is_balanced_tree.TreeNode(3)
    one.left = two
    two.left = three
    four = is_balanced_tree.TreeNode(4)
    five = is_balanced_tree.TreeNode(5)
    two.left = four
    four.left = five
    twenty = is_balanced_tree.TreeNode(20)
    one.right = twenty
    thirty = is_balanced_tree.TreeNode(30)
    twenty.right = thirty
    forty = is_balanced_tree.TreeNode(40)
    thirty.right = forty
    fifty = is_balanced_tree.TreeNode(50)
    forty.right = fifty

    assert False == is_balanced_tree.is_balanced_tree(one)


def test_is_balanced():
    three = is_balanced_tree.TreeNode(3)

    assert True == is_balanced_tree.is_balanced_tree(three)

    nine = is_balanced_tree.TreeNode(9)
    twenty = is_balanced_tree.TreeNode(20)
    fifteen = is_balanced_tree.TreeNode(15)
    seven = is_balanced_tree.TreeNode(7)

    three.left = nine
    assert True == is_balanced_tree.is_balanced_tree(three)

    three.right = twenty
    assert True == is_balanced_tree.is_balanced_tree(three)

    twenty.left = fifteen
    twenty.right = seven

    assert True == is_balanced_tree.is_balanced_tree(three)

    six = is_balanced_tree.TreeNode(6)
    seven.right = six

    assert False == is_balanced_tree.is_balanced_tree(three)

    eight = is_balanced_tree.TreeNode(8)
    seven.left = eight

    assert False == is_balanced_tree.is_balanced_tree(three)

    ten = is_balanced_tree.TreeNode(10)
    nine.right = ten

    assert True == is_balanced_tree.is_balanced_tree(three)

    assert True == is_balanced_tree.is_balanced_tree(None)
