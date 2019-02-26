from List import is_cycle


def test_is_cycle():
    head = is_cycle.LinkedNode(3)
    two = is_cycle.LinkedNode(2)
    zero = is_cycle.LinkedNode(0)
    four = is_cycle.LinkedNode(4)
    head.next = two
    two.next = zero
    zero.next = four
    four.next = two

    assert True == is_cycle.is_cycle(head)

def test_is_cycle_2():
    head = is_cycle.LinkedNode(3)
    two = is_cycle.LinkedNode(2)
    head.next = two
    assert False == is_cycle.is_cycle(head)