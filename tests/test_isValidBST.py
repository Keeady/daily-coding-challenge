from Tree import is_valid_bst
from library import node

def test_isValidBST_False():
    three = node.Node(3)
    six = node.Node(6)
    one = node.Node(1)
    four = node.Node(4, three, six)
    root = node.Node(5, one, four);

    solution = is_valid_bst.Solution()
    isValid = solution.isValidBST(root)
    assert isValid == False

def test_isValidBST_True():
    three = node.Node(3)
    one = node.Node(1)
    two = node.Node(2, one, three)

    solution = is_valid_bst.Solution()
    isValid = solution.isValidBST(two)
    assert isValid == True


def test_isValidBST_Null():
    six = node.Node(6)
    twenty = node.Node(20)
    five = node.Node(5)
    fifteen = node.Node(15, six, twenty)
    ten = node.Node(10, five, fifteen)

    solution = is_valid_bst.Solution()
    isValid = solution.isValidBST(ten)
    assert isValid == False


def test_isValidBST_Dup():
    one = node.Node(1)
    two = node.Node(1, one)

    solution = is_valid_bst.Solution()
    isValid = solution.isValidBST(two)
    assert isValid == False


def test_isValidBST_Neg():
    forty = node.Node(-45)
    twenty = node.Node(25, forty)
    thirty = node.Node(38, twenty)
    eight = node.Node(-80, None, thirty)

    solution = is_valid_bst.Solution()
    isValid = solution.isValidBST(eight)
    assert isValid == True

