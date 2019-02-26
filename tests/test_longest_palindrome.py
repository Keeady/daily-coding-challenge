from Trie import suffix_trie


def test_longest_pal():
    str = 'racecar'
    assert 7 == suffix_trie.longest_palindrome(str)
    assert 7 == suffix_trie.longest_palindrome('racecars')
    assert 5 == suffix_trie.longest_palindrome('bananas')
    assert 1 == suffix_trie.longest_palindrome('abcdefg')
    assert 3 == suffix_trie.longest_palindrome('abacdcgg')