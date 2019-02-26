from Most_Frequent_Words import find_k_frequent_words


def test_word_freq():
    book = "Zom Kim Bo bom bom Mi anchor is a smart smart, but self-centered TV tv anchor. Kim is a smart anchor. Mi zoom xoom zoom zoom bom Zom Zom Zom"
    k = 5
    delim = [',','.', ' ']

    words = find_k_frequent_words.find_frequent_words(k, book, delim, ['they', 'their', 'a'])
    expected_words = ['zom', 'bom', 'smart', 'anchor', 'zoom']
    for w in words:
        if w not in expected_words:
            assert False

    assert True