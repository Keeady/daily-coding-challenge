class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minimal_tree(input_array):
    if len(input_array) == 0:
        return None

    return build_minimal_tree(input_array, 0, len(input_array) - 1)


def build_minimal_tree(input_array, left, right):
    diff = right - left
    if diff == 0:
        return TreeNode(input_array[left])

    if diff < 0:
        return None

    mid = left + int((right - left) / 2)
    left_child = build_minimal_tree(input_array, left, mid - 1)
    right_child = build_minimal_tree(input_array, mid + 1, right)

    root = TreeNode(input_array[mid])
    root.left = left_child
    root.right = right_child

    return root