from Most_Frequent_Words import find_k_frequent_words
import heapq


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


def test_obj():
    book = 'me me me is me we'

    class freq:
        def __init__(self, text):
            self.text = text
            self.count = 1

        def increment(self):
            self.count += 1

    my_dict = {}
    me = freq('me')
    we = freq('we')
    my_dict['me'] = me
    my_dict['we'] = we

    freq_words = []
    heapq.heappush(freq_words, (me.count, me))
    heapq.heappush(freq_words, (we.count, we))

    me.increment()
    heapq.heapify(freq_words)
    we.increment()
    heapq.heapify(freq_words)
    we.increment()
    heapq.heapify(freq_words)



    print(freq_words[0].text)
    print(freq_words[1].text)

    assert False