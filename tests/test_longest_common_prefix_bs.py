from String import longest_common_prefix_binary_search


def test_longest_common_prefix():
    input = ['flower', 'flo', 'flow', 'flock']
    assert 'flo' == longest_common_prefix_binary_search.longest_common_prefix_binary_search(input)

    input = ['flower', 'flo', 'flow', 'flock', 'flight']
    assert 'fl' == longest_common_prefix_binary_search.longest_common_prefix_binary_search(input)

    input = ['flower', 'flo', 'flow', 'flock', 'manager']
    assert '' == longest_common_prefix_binary_search.longest_common_prefix_binary_search(input)

    input = []
    assert '' == longest_common_prefix_binary_search.longest_common_prefix_binary_search(input)

    input = ['', 'flower', 'flo', 'flow', 'flock', 'manager']
    assert '' == longest_common_prefix_binary_search.longest_common_prefix_binary_search(input)

    input = ['flowerdress', 'flowermaid', 'flowier', 'flowing', 'flockbird', 'flightattendant']
    assert 'fl' == longest_common_prefix_binary_search.longest_common_prefix_binary_search(input)
