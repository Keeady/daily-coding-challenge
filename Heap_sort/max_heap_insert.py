def insert(heap, distance):
    heap.append(distance)

    if len(heap) == 1:
        return heap

    return balance_heap(heap)


def balance_heap(heap):
    index = len(heap) - 1

    while index > 0:
        parent_index = int((index - 1) / 2)
        if heap[parent_index] < heap[index]:
            parent = heap[parent_index]
            heap[parent_index] = heap[index]
            heap[index] = parent

            index = parent_index

        else:
            return heap

    return heap
