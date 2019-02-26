import operator
from functools import reduce

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.total = val
        self.children = []


def main(arr, target):
    root = calc_combination_sum(arr, target)
    output = find_combinations(root, target)

    return [0]


def calc_combination_sum(arr, target):
    root = TreeNode(0)

    for i in range(0, len(arr)):
        if arr[i] == 0:
            continue

        if root.total + arr[i] <= target:
            node = TreeNode(arr[i])
            root.children.append(node)
            node.total += root.total

            calc_node_combination(node, arr, target)

    return root


def find_combinations(root, target):
    if len(root.children) == 0:
        if root.total == target:
            return [root.val]
        return []

    output = []
    for node in root.children:
        node_list = find_combinations(node, target)

        if node_list and len(node_list) > 0:
            if root.val > 0:
                node_list.append(root.val)
                output.append(node_list)

    return output


def calc_node_combination(root, arr, target):
    for i in range(0, len(arr)):
        if arr[i] == 0:
            continue

        if root.total + arr[i] <= target:
            node = TreeNode(arr[i])
            root.children.append(node)
            node.total += root.total

    for node in root.children:
        calc_node_combination(node, arr, target)

    return root
