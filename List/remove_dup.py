class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, node: LinkedListNode):
        self.head = node

class ListDedup:

    def remove_list_dup(self, list: LinkedList):
        if list.head is None:
            return None

        head = list.head
        node_dict = {}
        node_dict[head.data] = True

        while head is not None and head.next is not None:
            # check if in dictionary
            if head.next.data in node_dict:
                next_pointer = head.next.next
                head.next.next = None
                head.next = next_pointer

            # add to dictionary
            else:
                node_dict[head.next.data] = True

            head = head.next

        return list


    def remove_list_dup_nobuffer(self, list: LinkedList):
        if list.head is None:
            return None

        pointer1 = list.head
        pointer2 = list.head

        while pointer1 is not None:
            pointer2 = pointer1
            while pointer2 is not None and pointer2.next is not None:
                if pointer1.data == pointer2.next.data:
                    next_pointer = pointer2.next.next
                    pointer2.next.next = None
                    pointer2.next = next_pointer

                pointer2 = pointer2.next

            pointer1 = pointer1.next
        return list