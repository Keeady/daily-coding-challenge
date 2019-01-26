# in a sorted list, remove all nodes that have duplicates
# use a constant buffer to keep track of the value of the current duplicate sub list
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head: LinkedListNode):
    if head is None or head.next is None:
        return head

    duplicate_value = None
    current = head
    prev = None

    while current is not None:
        if current.next is not None and current.data == current.next.data:
            duplicate_value = current.data

        if duplicate_value == current.data:
            next = current.next
            current.next = None
            if prev is None:
                head = next
            else:
                prev.next = next

            current = next

        else:
            prev = current
            current = current.next

    return head