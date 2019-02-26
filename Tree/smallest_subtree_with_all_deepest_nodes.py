import queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_max_level(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return max(find_max_level(root.left), find_max_level(root.right)) + 1


def  find_max_level_subtree(root, level_dict):
    if not root:
        return 0

    if root.val not in level_dict:
        level_dict[root.val] = 1

    if not root.left and not root.right:
        return level_dict[root.val]

    max_left = 0
    max_right = 0

    if root.left:
        level_dict[root.left.val] = level_dict[root.val] + 1
        max_left = find_max_level_subtree(root.left, level_dict)

    if root.right:
        level_dict[root.right.val] = level_dict[root.val] + 1
        max_right = find_max_level_subtree(root.right, level_dict)

    return max(max_left, max_right)


def find_max_subtree(root, level_dict):
    if not root:
        return None

    if root.val not in level_dict:
        level_dict[root.val] = 1

    if not root.left and not root.right:
        return root

    max_left = None
    max_right = None

    if root.left:
        level_dict[root.left.val] = level_dict[root.val] + 1
        max_left = find_max_subtree(root.left, level_dict)

    if root.right:
        level_dict[root.right.val] = level_dict[root.val] + 1
        max_right = find_max_subtree(root.right, level_dict)

    if max_left is not None and max_right is not None:
        if level_dict[max_left.val] == level_dict[max_right.val]:
            level_dict[root.val] = level_dict[max_left.val]

            return root
        elif level_dict[max_left.val] < level_dict[max_right.val]:
            return max_right
        else:
            return max_left
    elif max_left:
        return max_left
    elif max_right:
        return max_right


def find_max_subtree_no_extra_space(root):
    left_height = find_max_level(root.left)
    right_height = find_max_level(root.right)

    if left_height == right_height:
        return root

    if left_height > right_height:
        return find_max_subtree_no_extra_space(root.left)

    return find_max_subtree_no_extra_space(root.right)


# what to do when more than one is deepest
def find_deepest_node_bfs(root):
    node_queue = queue.Queue()
    node_queue.put(root)
    visited = {}
    node = root

    while not node_queue.empty():
        node = node_queue.get()
        visited[node] = True

        if node.left and node.left not in visited:
            node_queue.put(node.left)

        if node.right and node.right not in visited:
            node_queue.put(node.right)

    return node
