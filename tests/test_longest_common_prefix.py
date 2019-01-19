from String import longest_common_prefix


def test_longest_common_prefix():
    input = ['flower', 'flo', 'flow', 'flock']
    assert 'flo' == longest_common_prefix.longest_common_prefix(input)

    input = ['flower', 'flo', 'flow', 'flock', 'flight']
    assert 'fl' == longest_common_prefix.longest_common_prefix(input)

    input = ['flower', 'flo', 'flow', 'flock', 'manager']
    assert '' == longest_common_prefix.longest_common_prefix(input)

    input = []
    assert '' == longest_common_prefix.longest_common_prefix(input)

    input = ['', 'flower', 'flo', 'flow', 'flock', 'manager']
    assert '' == longest_common_prefix.longest_common_prefix(input)