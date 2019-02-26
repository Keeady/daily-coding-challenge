from List import node_cycle_start


def test_is_cycle():
    head = node_cycle_start.LinkedNode(3)
    two = node_cycle_start.LinkedNode(2)
    zero = node_cycle_start.LinkedNode(0)
    four = node_cycle_start.LinkedNode(4)
    head.next = two
    two.next = zero
    zero.next = four
    four.next = two

    node = node_cycle_start.find_node_cycle(head)
    assert node.val == 2

def test_is_cycle_2():
    head = node_cycle_start.LinkedNode(3)
    two = node_cycle_start.LinkedNode(2)
    head.next = two
    node = node_cycle_start.find_node_cycle(head)
    assert node is None

def test_is_cycle_3():
    head = node_cycle_start.LinkedNode(3)
    two = node_cycle_start.LinkedNode(2)
    zero = node_cycle_start.LinkedNode(0)
    four = node_cycle_start.LinkedNode(4)
    head.next = two
    two.next = zero
    zero.next = four
    four.next = zero

    node = node_cycle_start.find_node_cycle(head)
    assert node.val == 0
