from Tree import isSymetricTree
from library import node



def test_getLevel():
    five = node.Node(5)
    four = node.Node(4)
    two = node.Node(2, four, five)
    three = node.Node(3)
    one = node.Node(1, two, three)

    solution = isSymetricTree.Solution()
    result = solution.getLevel(one, 0, {})
    assert result == {0:[two, three], 1: [four,five, None, None], 2: [None, None, None, None]}

def test_asymetry():
    five = node.Node(5)
    four = node.Node(4)
    two = node.Node(2, four, five)
    three = node.Node(3)
    one = node.Node(1, two, three)

    solution = isSymetricTree.Solution()
    result = solution.isSymetric(one)
    assert result == False

def test_asymetryTrue():
    eight = node.Node(8)
    eight_2 = node.Node(8)
    seven = node.Node(7)
    seven_2 = node.Node(7)
    six = node.Node(6)
    six_2 = node.Node(6)
    five = node.Node(5)
    five_2 = node.Node(5)
    three = node.Node(3, eight, seven)
    three_2 = node.Node(3, seven_2, eight_2)
    four = node.Node(4, six, five)
    four_2 = node.Node(4, five_2, six_2)
    two = node.Node(2, three, four)
    two_2 = node.Node(2, four_2, three_2)
    one = node.Node(1, two, two_2)

    solution = isSymetricTree.Solution()
    result = solution.isSymetric(one)
    assert result == True

def test_asymetry_with_null():
    three = node.Node(3)
    three_2 = node.Node(3)
    two = node.Node(2, three)
    two_2 = node.Node(2, None, three_2)
    one = node.Node(1, two, two_2)

    solution = isSymetricTree.Solution()
    result = solution.isSymetric(one)
    assert result == True

def test_not_asymetry():
    three = node.Node(3)
    three_2 = node.Node(3)
    two = node.Node(2, None, three)
    two_2 = node.Node(2, None, three_2)
    one = node.Node(1, two, two_2)

    solution = isSymetricTree.Solution()
    result = solution.isSymetric(one)
    assert result == False

def test_sym_tree():
    three = node.Node(3)
    three_2 = node.Node(3)
    two = node.Node(2, None, three)
    two_2 = node.Node(2, None, three_2)
    one = node.Node(1, two, two_2)

    solution = isSymetricTree.Solution()
    result = solution.isSymetricTree(one)
    assert result == False

def test_sym_tree_2():
    three = node.Node(3)
    three_2 = node.Node(3)
    two = node.Node(2, three)
    two_2 = node.Node(2, None, three_2)
    one = node.Node(1, two, two_2)

    solution = isSymetricTree.Solution()
    result = solution.isSymetricTree(one)
    assert result == True

def test_sym_tree_3():
    three = node.Node(3)
    two = node.Node(2)
    one = node.Node(1, two, three)

    solution = isSymetricTree.Solution()
    result = solution.isSymetricTree(one)
    assert result == False