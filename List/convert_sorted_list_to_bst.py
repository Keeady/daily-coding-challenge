class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def convert(head: ListNode):
    if head is None:
        return None

    length = get_length(head)
    left = 0
    right = length - 1

    root = build_bst(head, left, right)

    return root[1]


def build_bst(head, left, right):
    if right - left == 1:
        # right is root, left is left child
        root = TreeNode(head.next.val)
        root.left = TreeNode(head.val)

        return [head.next, root]

    if right == left:
        # return leaf
        root = TreeNode(head.val)

        return [head, root]

    # at least 3 elements

    mid = left + (right - left) // 2
    left_children = build_bst(head, left, mid - 1)
    left_head = left_children[0]
    left_root = left_children[1]

    # moving head
    head = left_head.next
    root = TreeNode(head.val)
    root.left = left_root

    right_children = build_bst(head.next, mid + 1, right)
    right_head = right_children[0]
    right_root = right_children[1]
    root.right = right_root

    return [right_head, root]


def get_length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next

    return count