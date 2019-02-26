def remove(heap):
    last_distance = heap.pop()

    if len(heap) == 0:
        return heap

    heap[0] = last_distance

    i = 0
    while i < len(heap):
        parent = heap[i]
        left_child = i * 2 + 1
        right_child = i * 2 + 2
        child_index = left_child

        if right_child < len(heap):
            if heap[right_child] > heap[left_child]:
                child_index = right_child
        elif left_child < len(heap):
            child_index = left_child
        else:
            return heap

        if parent < heap[child_index]:
            heap[i] = heap[child_index]
            heap[child_index] = parent
        else:
            return heap

        i += 1

    return heap