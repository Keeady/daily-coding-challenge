import queue

#modified bfs
# find max level in the tree and initialize array of corresponding size
# alternatively, prepend
# find all nodes for a given level

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print(root):
    if not root:
        return []

    levels = find_max_level(root)

    node_queue = queue.Queue()
    node_queue.put(root)
    node_list = [0] * levels

    level_index = levels - 1
    while not node_queue.empty():
        nodes = print_level(node_queue)
        node_values = print_next_level(nodes, node_queue)
        node_list[level_index] = node_values

        level_index -= 1

    return node_list


def find_max_level(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return max(find_max_level(root.left), find_max_level(root.right)) + 1


def print_level(node_queue):
    nodes = []
    while not node_queue.empty():
        nodes.append(node_queue.get())

    return nodes


def print_next_level(nodes, node_queue):
    node_values = []
    for node in nodes:
        if node.left:
            node_queue.put(node.left)

        if node.right:
            node_queue.put(node.right)

        node_values.append(node.val)

    return node_values