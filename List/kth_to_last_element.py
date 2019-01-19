class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_kth_to_last_element(list: LinkedListNode, k):
    if list is None:
        return None

    if k == 0:
        return list

    # find length of list
    head = list
    runner = list
    node_count = 0
    while runner is not None:
        node_count += 1
        runner = runner.next

    stop = node_count - k
    start = 0
    while start < stop:
        start += 1
        head = head.next

    return head


def find_kth_to_last(list: LinkedListNode, k):
    if list is None:
        return None

    if k == 0:
        return list

    # move runner k ahead
    head = list
    runner = list
    node_count = 0
    while node_count < k:
        node_count += 1
        if runner is None:
            return None

        runner = runner.next

    while runner is not None:
        runner = runner.next
        head = head.next

    return head