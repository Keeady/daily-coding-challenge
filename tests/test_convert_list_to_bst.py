from List import convert_sorted_list_to_bst


def test_convert_basic():
    assert None == convert_sorted_list_to_bst.convert(None)

    head = convert_sorted_list_to_bst.ListNode(89)
    root = convert_sorted_list_to_bst.convert(head)
    assert root.val == 89

def test_convert():
    head = convert_sorted_list_to_bst.ListNode(-10)
    three = convert_sorted_list_to_bst.ListNode(-3)
    head.next = three

    zero = convert_sorted_list_to_bst.ListNode(0)
    three.next = zero

    five = convert_sorted_list_to_bst.ListNode(5)
    zero.next = five
    nine = convert_sorted_list_to_bst.ListNode(9)
    five.next = nine

    root = convert_sorted_list_to_bst.convert(head)
    assert root.val == 0
    assert root.left.val == -3
    assert root.right.val == 9
    left = root.left
    assert left.right is None
    assert left.left.val == -10
    right = root.right
    assert right.left.val == 5
    assert right.right is None

def test_convert_2():
    head = convert_sorted_list_to_bst.ListNode(100)
    three = convert_sorted_list_to_bst.ListNode(101)
    head.next = three

    zero = convert_sorted_list_to_bst.ListNode(102)
    three.next = zero

    four = convert_sorted_list_to_bst.ListNode(103)
    zero.next = four

    five = convert_sorted_list_to_bst.ListNode(104)
    four.next = five

    six = convert_sorted_list_to_bst.ListNode(105)
    five.next = six

    seven = convert_sorted_list_to_bst.ListNode(106)
    six.next = seven

    eight = convert_sorted_list_to_bst.ListNode(107)
    seven.next = eight

    nine = convert_sorted_list_to_bst.ListNode(108)
    eight.next = nine

    nine.next = convert_sorted_list_to_bst.ListNode(109)

    root = convert_sorted_list_to_bst.convert(head)
    assert root.val == 104
    assert root.left.val == 101
    assert root.right.val == 107

    left = root.left
    assert left.right is not None
    assert left.left is not None
    assert left.right.val == 103
    assert left.left.val == 100

    right = root.right
    assert right.left.val == 106
    assert right.right.val == 109

    left_2 = left.left
    assert left_2.left is None
    assert left_2.right is None

    right_2 = left.right
    assert right_2.left.val == 102
    assert right_2.right is None

    left_3 = right_2.left
    assert left_3.left is None
    assert left_3.right is None

    six = right.left
    assert six.left.val == 105
    assert six.right is None

    nine = right.right
    assert nine.right is None
    assert nine.left.val == 108

    eight = nine.left
    assert eight.left is None
    assert eight.right is None