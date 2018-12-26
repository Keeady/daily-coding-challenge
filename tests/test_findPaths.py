from Tree import sumRootToLeaf
from library import node

def test_sum():
    one = node.Node(1)
    five = node.Node(5)
    zero = node.Node(0)
    nine = node.Node(9, five, one)
    four = node.Node(4, nine, zero)


    solution = sumRootToLeaf.Solution()
    result = solution.sumRootToLeaf(four)

    assert result == 1026

def test_sum_zero():
    solution = sumRootToLeaf.Solution()
    result = solution.sumRootToLeaf(None)

    assert result == 0

def test_sum_root():
    four = node.Node(4)

    solution = sumRootToLeaf.Solution()
    result = solution.sumRootToLeaf(four)

    assert result == 4

def test_sum_one_child():
    nine = node.Node(9)
    four = node.Node(4, nine)

    solution = sumRootToLeaf.Solution()
    result = solution.sumRootToLeaf(four)

    assert result == 49

def test_sum_two():
    zero = node.Node(8)
    nine = node.Node(9)
    four = node.Node(4, nine, zero)


    solution = sumRootToLeaf.Solution()
    result = solution.sumRootToLeaf(four)

    assert result == 97

def test_sum_right_child():
    nine = node.Node(9)
    four = node.Node(4, None, nine)

    solution = sumRootToLeaf.Solution()
    result = solution.sumRootToLeaf(four)

    assert result == 49

def test_sum_right():
    one = node.Node(1)
    five = node.Node(5)
    zero = node.Node(0)
    nine = node.Node(9, five, one)
    four = node.Node(4, zero, nine)


    solution = sumRootToLeaf.Solution()
    result = solution.sumRootToLeaf(four)

    assert result == 1026