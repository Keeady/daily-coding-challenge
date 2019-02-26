from Trie import suffix_trie


def test_suffix_trie():
    str = 'racecar'
    root = suffix_trie.build_suffix_trie(str)
    assert len(root.children) == 4
    assert root.children['r'] is not None
    assert root.children['a'] is not None
    assert root.children['c'] is not None
    assert root.children['e'] is not None

    r = root.children['r']
    assert len(r.children) == 1
    a = r.children['a']
    assert len(a.children) == 1

    a = root.children['a']
    assert len(a.children) == 2
    assert a.children['c'] is not None
    assert a.children['r'] is not None

    c = root.children['c']
    assert len(c.children) == 2
    assert c.children['e'] is not None
    assert c.children['a'] is not None

    e = root.children['e']
    assert len(e.children) == 1
    assert e.children['c'] is not None

