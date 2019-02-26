class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sorted_array_to_bst(arr):
    return bst(arr, 0, len(arr) - 1)


def bst(arr, low, high):
    if high - low == 1:
        root = TreeNode(arr[high])
        root.left = TreeNode(arr[low])

        return root

    if low == high:
        return TreeNode(arr[low])

    mid = low + (high - low) // 2

    root = TreeNode(arr[mid])
    root.left = bst(arr, low, mid - 1)
    root.right = bst(arr, mid + 1, high)

    return root