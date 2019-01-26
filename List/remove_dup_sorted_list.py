# given sorted linked list
# removing duplicates using 2 pointers
# 1 pointer ahead and compare current and next
# if dup, move fast pointer ahead
# if not dup move slow pointer ahead also
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head: LinkedListNode):
    if head is None or head.next is None:
        return head

    current = head

    while current is not None and current.next is not None:
        if current.data == current.next.data:
            next = current.next.next
            current.next.next = None
            current.next = next
        else:
            current = current.next

    return head