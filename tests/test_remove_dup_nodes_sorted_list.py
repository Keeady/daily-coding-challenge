from List import remove_dup_nodes


def test_remove_dup():
    one = remove_dup_nodes.LinkedListNode(1)
    one_1 = remove_dup_nodes.LinkedListNode(1)
    two = remove_dup_nodes.LinkedListNode(2)
    three = remove_dup_nodes.LinkedListNode(3)
    four = remove_dup_nodes.LinkedListNode(4)
    one.next = one_1
    one_1.next = two
    two.next = three
    three.next = four

    head = remove_dup_nodes.remove_duplicates(one)

    assert 2 == head.data
    assert 3 == head.next.data

def test_remove_all_dup():
    one = remove_dup_nodes.LinkedListNode(1)
    one_1 = remove_dup_nodes.LinkedListNode(1)
    two = remove_dup_nodes.LinkedListNode(1)
    three = remove_dup_nodes.LinkedListNode(1)
    four = remove_dup_nodes.LinkedListNode(1)
    one.next = one_1
    one_1.next = two
    two.next = three
    three.next = four

    head = remove_dup_nodes.remove_duplicates(one)

    assert None is head

def test_remove_no_dup():
    one = remove_dup_nodes.LinkedListNode(1)
    two = remove_dup_nodes.LinkedListNode(2)
    three = remove_dup_nodes.LinkedListNode(3)
    four = remove_dup_nodes.LinkedListNode(4)
    one.next = two
    two.next = three
    three.next = four

    head = remove_dup_nodes.remove_duplicates(one)

    assert 1 == head.data
    assert 2 == head.next.data

def test_remove_one_dup():
    one = remove_dup_nodes.LinkedListNode(1)
    two = remove_dup_nodes.LinkedListNode(2)
    two_2 = remove_dup_nodes.LinkedListNode(2)
    three = remove_dup_nodes.LinkedListNode(3)
    four = remove_dup_nodes.LinkedListNode(4)
    one.next = two
    two.next = two_2
    two_2.next = three
    three.next = four

    head = remove_dup_nodes.remove_duplicates(one)

    assert 1 == head.data
    assert 3 == head.next.data
