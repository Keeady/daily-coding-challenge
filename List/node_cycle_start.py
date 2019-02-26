class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_node_cycle(head):
    if not head:
        return None

    left = head
    right = head
    while right and right.next:
        left = left.next
        right = right.next.next

        if left == right:
            right = head
            while right != left:
                right = right.next
                left = left.next

            return right

    return None

