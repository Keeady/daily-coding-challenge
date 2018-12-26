from Tree import closestValueBST
from library import node

def test_find_same_value():
    thirteen = node.Node(13)
    twenty = node.Node(20)
    five = node.Node(5)
    fifteen = node.Node(15, thirteen, twenty)
    ten = node.Node(10, five, fifteen)

    solution = closestValueBST.Solution()
    result = solution.findClosestValue(ten, 13)
    assert result == 13

def test_find_closest_value():
    eleven = node.Node(11)
    twenty = node.Node(20)
    five = node.Node(5)
    fifteen = node.Node(15, eleven, twenty)
    ten = node.Node(10, five, fifteen)

    solution = closestValueBST.Solution()
    result = solution.findClosestValue(ten, 13)
    assert result == 15

def test_find_closest_value_left():
    four = node.Node(4)
    eight = node.Node(8)
    one = node.Node(1, None, four)
    eleven = node.Node(11)
    twenty = node.Node(20)
    five = node.Node(5, one, eight)
    fifteen = node.Node(15, eleven, twenty)
    ten = node.Node(10, five, fifteen)

    solution = closestValueBST.Solution()
    result = solution.findClosestValue(ten, 7)
    assert result == 8

def test_find_closest_value_left_same():
    four = node.Node(4)
    eight = node.Node(8)
    one = node.Node(1, None, four)
    eleven = node.Node(11)
    twenty = node.Node(20)
    five = node.Node(5, one, eight)
    fifteen = node.Node(15, eleven, twenty)
    ten = node.Node(10, five, fifteen)

    solution = closestValueBST.Solution()
    result = solution.findClosestValue(ten, 4)
    assert result == 4

def test_find_closest_value_left_close():
    four = node.Node(4)
    eight = node.Node(8)
    one = node.Node(1, None, four)
    eleven = node.Node(11)
    twenty = node.Node(20)
    five = node.Node(5, one, eight)
    fifteen = node.Node(15, eleven, twenty)
    ten = node.Node(10, five, fifteen)

    solution = closestValueBST.Solution()
    result = solution.findClosestValue(ten, 3)
    assert result == 4

def test_find_closest_value_left_right():
    four = node.Node(4)
    eight = node.Node(8)
    one = node.Node(1, None, four)
    eleven = node.Node(11)
    twenty = node.Node(20)
    five = node.Node(5, one, eight)
    fifteen = node.Node(15, eleven, twenty)
    ten = node.Node(10, five, fifteen)

    solution = closestValueBST.Solution()
    result = solution.findClosestValue(ten, 2)
    assert result == 1

