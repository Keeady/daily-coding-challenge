from Array import sorted_array_to_bst


def test_sorted_arr_bst():
    arr = [-10,-3,0,5,9]
    root = sorted_array_to_bst.sorted_array_to_bst(arr)
    assert root is not None
    assert root.val == 0
    assert root.left.val == -3
    assert root.right.val == 9
    assert root.left.left.val == -10
    assert root.right.left.val == 5
    assert root.left.right is None
    assert root.right.right is None