class TreeNode:
    def __init__(self, val, parent):
        self.val = val
        #self.parent = parent
        self.children = {}

def create_folder_path_tree(paths):
    # relative to root or a given directory
    # empty string is not valid path
    # path starting with slash
    # path with no slash
    # ../.. in path
    # hidden paths

    root = TreeNode('/', None)

    for path in paths:
        folders = path.split('/')
        node = root

        parents = [root]

        for folder in folders:
            if len(folder) == 0:
                continue

            if folder == '..':
                node = find_parent_node(parents)
                continue
            else:
                next_node = find_path_node(folder, node)

            if next_node is None:
                # create node
                next_node = create_path_node(folder, node)

            node = next_node
            parents.append(node)

    return root


def find_parent_node(parents):
    if len(parents) > 1:
        parents.pop()

    return parents[len(parents) - 1]


def print_folder_path_tree(root):
    pass


def find_path_node(path, root):
    if root.val == path:
        return root

    if path in root.children:
        return root.children[path]

    return None


def create_path_node(path, root):
    if path in root.children:
        return root.children[path]

    root.children[path] = TreeNode(path, root)

    return root.children[path]