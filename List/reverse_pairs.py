class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_pairs(head):
    if head is None:
        return

    p1 = head
    prev = None

    while p1 and p1.next is not None:
        p2 = p1.next
        p1.next = p2.next
        p2.next = p1

        if prev is not None:
            prev.next = p2
        else:
            head = p2

        prev = p1
        p1 = p1.next

    return head

def array_to_list(arr):
    head = ListNode(arr[0])
    prev = head
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        prev.next = node
        prev = prev.next

    return head

def print(head):
    mlist = []
    while head is not None:
        mlist.append(head.val)
        head = head.next

    return mlist