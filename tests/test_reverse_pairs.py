from List import reverse_pairs


def test_reverse():
    head = reverse_pairs.array_to_list([5,2,4,3,1])
    assert head.val == 5
    assert head.next.val == 2
    assert head.next.next.val == 4
    assert head.next.next.next.val == 3
    assert head.next.next.next.next.val == 1

    head = reverse_pairs.reverse_pairs(head)
    assert head.val == 2
    assert head.next.val == 5
    assert head.next.next.val == 3
    assert head.next.next.next.val == 4
    assert head.next.next.next.next.val == 1

    mlist = reverse_pairs.print(head)

    assert mlist == [2,5,3,4,1]
