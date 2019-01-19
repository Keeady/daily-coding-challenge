from List import kth_to_last_element


def test_kth_to_last():
    one = kth_to_last_element.LinkedListNode(1)
    two = kth_to_last_element.LinkedListNode(4)
    one.next = two
    three = kth_to_last_element.LinkedListNode(2)
    two.next = three
    four = kth_to_last_element.LinkedListNode(8)
    three.next = four
    five = kth_to_last_element.LinkedListNode(4)
    four.next = five
    six = kth_to_last_element.LinkedListNode(1)
    five.next = six

    kth = kth_to_last_element.find_kth_to_last_element(one, 2)
    assert kth.data == 4

    kth = kth_to_last_element.find_kth_to_last(one, 2)
    assert kth.data == 4

    kth = kth_to_last_element.find_kth_to_last_element(one, 1)
    assert kth.data == 1

    kth = kth_to_last_element.find_kth_to_last(one, 1)
    assert kth.data == 1

    kth = kth_to_last_element.find_kth_to_last_element(one, 4)
    assert kth.data == 2

    kth = kth_to_last_element.find_kth_to_last(one, 4)
    assert kth.data == 2

    kth = kth_to_last_element.find_kth_to_last_element(one, 6)
    assert kth.data == 1

    kth = kth_to_last_element.find_kth_to_last(one, 6)
    assert kth.data == 1

    kth = kth_to_last_element.find_kth_to_last_element(one, 10)
    assert kth is one

    kth = kth_to_last_element.find_kth_to_last(one, 10)
    assert kth is None