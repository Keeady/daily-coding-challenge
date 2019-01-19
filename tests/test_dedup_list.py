from List import remove_dup


def test_remove_no_dup():
    head = remove_dup.LinkedListNode(1)
    list = remove_dup.LinkedList(head)

    dedup = remove_dup.ListDedup()
    dedup_list = dedup.remove_list_dup(list)
    assert dedup_list.head.data == 1

    dedup_list = dedup.remove_list_dup_nobuffer(list)
    assert dedup_list.head.data == 1

def test_remove_root_dup():
    head = remove_dup.LinkedListNode(1)
    head.next = remove_dup.LinkedListNode(1)
    list = remove_dup.LinkedList(head)

    dedup = remove_dup.ListDedup()
    dedup_list = dedup.remove_list_dup(list)
    assert dedup_list.head.data == 1
    assert dedup_list.head.next is None

    dedup_list = dedup.remove_list_dup_nobuffer(list)
    assert dedup_list.head.data == 1
    assert dedup_list.head.next is None

def test_remove_mid_dup():
    head = remove_dup.LinkedListNode(1)
    head.next = remove_dup.LinkedListNode(1)
    head.next.next = remove_dup.LinkedListNode(2)
    list = remove_dup.LinkedList(head)

    dedup = remove_dup.ListDedup()
    dedup_list = dedup.remove_list_dup(list)
    assert dedup_list.head.data == 1
    assert dedup_list.head.next.data == 2

    dedup_list = dedup.remove_list_dup_nobuffer(list)
    assert dedup_list.head.data == 1
    assert dedup_list.head.next.data == 2