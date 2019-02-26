from Tree import max_path_sum


def test_sum():
    one = max_path_sum.TreeNode(1)
    two = max_path_sum.TreeNode(2)
    three = max_path_sum.TreeNode(3)
    four = max_path_sum.TreeNode(4)
    five = max_path_sum.TreeNode(-5)
    one.left = two
    one.right = three
    two.left = four
    two.right = five

    assert 10 == max_path_sum.path_sum(one)



def test_calc_sum_tree():
    one = max_path_sum.TreeNode(1)
    two = max_path_sum.TreeNode(2)
    three = max_path_sum.TreeNode(3)
    four = max_path_sum.TreeNode(4)
    five = max_path_sum.TreeNode(5)
    one.left = two
    one.right = three
    two.left = four
    two.right = five

    assert 15 == max_path_sum.path_sum(one)


def test_calc_tree():
    one = max_path_sum.TreeNode(-1)
    two = max_path_sum.TreeNode(2)
    three = max_path_sum.TreeNode(3)
    four = max_path_sum.TreeNode(-4)
    five = max_path_sum.TreeNode(-5)
    one.left = two
    one.right = three
    two.left = four
    two.right = five

    assert 4 == max_path_sum.path_sum(one)


def test_calc_neg_tree():
    one = max_path_sum.TreeNode(-2)
    two = max_path_sum.TreeNode(-1)

    one.left = two
    one.right = None
    two.left = None
    two.right = None

    assert -1 == max_path_sum.path_sum(one)


def test_calc_neg():
    one = max_path_sum.TreeNode(-2934)

    one.left = None
    one.right = None

    assert -2934 == max_path_sum.path_sum(one)

    assert 0 == max_path_sum.path_sum(None)


def test_calc_sum():
    one = max_path_sum.TreeNode(-1)
    two = max_path_sum.TreeNode(-2)
    three = max_path_sum.TreeNode(-3)
    one.left = two
    one.right = three

    four = max_path_sum.TreeNode(1)
    five = max_path_sum.TreeNode(3)
    two.left = four
    two.right = five

    six = max_path_sum.TreeNode(-2)
    seven = max_path_sum.TreeNode(-1)

    four.left = seven
    three.left = six

    assert 3 == max_path_sum.path_sum(one)


def test_calc_sum_2():
    one = max_path_sum.TreeNode(2)
    two = max_path_sum.TreeNode(-1)
    three = max_path_sum.TreeNode(-2)
    one.left = two
    one.right = three

    assert 2 == max_path_sum.path_sum(one)