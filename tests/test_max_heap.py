from Heap_sort import max_heap_insert, max_heap_remove


def test_max_heap_insert():
    assert [14] == max_heap_insert.insert([], 14)
    assert [20,14] == max_heap_insert.insert([14], 20)
    assert [20,14,2] == max_heap_insert.insert([20,14], 2)
    assert [20, 15, 2, 14] == max_heap_insert.insert([20, 14, 2], 15)
    assert [20, 15, 2, 14, 10] == max_heap_insert.insert([20, 15, 2, 14], 10)
    assert [21, 15, 20, 14, 10, 2] == max_heap_insert.insert([20, 15, 2, 14, 10], 21)


def test_max_heap_remove():
    assert [20, 15, 2, 14, 10] == max_heap_remove.remove([21, 15, 20, 14, 10, 2])
    assert [15, 14, 2, 10] == max_heap_remove.remove([20, 15, 2, 14, 10])