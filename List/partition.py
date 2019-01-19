def partition(head, k):
    if head is None:
        return None

    pointer = head
    prev = None

    while pointer is not None:
        if pointer.data < k:
            node = pointer.next
            pointer.next = node.next
            node.next = pointer
            pointer = node
        elif pointer.data > k:


