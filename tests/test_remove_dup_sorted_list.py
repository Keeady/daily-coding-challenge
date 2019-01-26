from List import remove_dup_sorted_list


def test_remove_no_dup():
    one = remove_dup_sorted_list.LinkedListNode(1)
    two = remove_dup_sorted_list.LinkedListNode(2)
    three = remove_dup_sorted_list.LinkedListNode(3)
    four = remove_dup_sorted_list.LinkedListNode(4)
    one.next = two
    two.next = three
    three.next = four

    head = remove_dup_sorted_list.remove_duplicates(one)

    assert 1 == head.data
    assert 2 == head.next.data


def test_remove_dup():
    one = remove_dup_sorted_list.LinkedListNode(1)
    one_1 = remove_dup_sorted_list.LinkedListNode(1)
    two = remove_dup_sorted_list.LinkedListNode(2)
    three = remove_dup_sorted_list.LinkedListNode(3)
    four = remove_dup_sorted_list.LinkedListNode(4)
    one.next = one_1
    one_1.next = two
    two.next = three
    three.next = four

    head = remove_dup_sorted_list.remove_duplicates(one)

    assert 1 == head.data
    assert 2 == head.next.data

def test_remove_all_dup():
    one = remove_dup_sorted_list.LinkedListNode(1)
    one_1 = remove_dup_sorted_list.LinkedListNode(1)
    two = remove_dup_sorted_list.LinkedListNode(1)
    three = remove_dup_sorted_list.LinkedListNode(1)
    four = remove_dup_sorted_list.LinkedListNode(1)
    one.next = one_1
    one_1.next = two
    two.next = three
    three.next = four

    head = remove_dup_sorted_list.remove_duplicates(one)

    assert 1 == head.data
    assert None is head.next
