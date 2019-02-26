import queue
class SuffixTrie:
    def __init__(self, val):
        self.val = val
        self.children = {}

    def find(self, str):
        if str in self.children:
            return self.children[str]
        return None


def build_suffix_trie(word):
    root = SuffixTrie('*')
    node_queue = queue.Queue()

    for char in word:
        if char not in root.children:
            char_node = SuffixTrie(char)
            root.children[char] = char_node
        else:
            char_node = root.children[char]

        max_length = node_queue.qsize()
        i = 0
        while i < max_length:
            node = node_queue.get()

            if char not in node.children:
                new_node = SuffixTrie(char)
                node.children[char] = new_node
                node_queue.put(new_node)

            i += 1

        node_queue.put(char_node)

    return root


def longest_palindrome(str):
    root = build_suffix_trie(str)

    start = len(str)
    node = root
    max_length = 0

    for i in range(len(str) - 1, -1, -1):
        char = str[i]

        next_node = node.find(char)
        if next_node is None:
            start = i + 1
            next_node = root.find(char)
        else:
            max_length = max(max_length, start - i)

        node = next_node

    return max_length