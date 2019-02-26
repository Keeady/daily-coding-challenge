class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_cycle(head):
    if not head:
        return False

    left = head
    right = head.next
    while right is not None:
        if left == right or left == right.next:
            return True

        if not left or not right.next or not right.next.next:
            return False

        left = left.next
        right = right.next.next

    return False