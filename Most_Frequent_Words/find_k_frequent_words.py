from heapq import heappush, heappop

class WordItem:
    def __init__(self, key):
        self.frequency = 1
        self.index = -1
        self.key = key

class HeapItem:
    def __init__(self, key, frequency):
        self.frequency = frequency
        self.key = key

def find_frequent_words(k, book, delimiters, ignore_words):
    start = 0
    end = 0
    word_frequency = {}
    delimiter_dict = build_del_dict(delimiters)
    ignore_dict = build_del_dict(ignore_words)
    heap = []
    frequent_words = []

    while start < len(book):
        if book[start] in delimiter_dict:
            start += 1
            continue

        end = start + 1
        while end < len(book) and book[end] not in delimiter_dict:
            end += 1

        key = ''.join(book[start:end])
        key = key.lower()

        if key in ignore_dict:
            start = end
            continue

        if key not in word_frequency:
            word = WordItem(key)
            word_frequency[key] = word
        else:
            word = word_frequency[key]
            word.frequency += 1

        print(key, ' :index in heap: ', word.index)

        if word.index >= 0:
            heap[word.index].frequency = word.frequency
            heap = heapify(heap, len(heap) - 1, word_frequency)
        else:
            heap = add_heap(k, heap, word, word_frequency)

        start = end

    print('**______________________')
    for key in word_frequency:
        print(word_frequency[key].key, word_frequency[key].frequency)

    print('**______________________')
    for i in range(len(heap) - 1, -1, -1):
        frequent_words.append(heap[i].key)
        print(heap[i].key, word_frequency[heap[i].key].frequency)

    return frequent_words


def heapify(heap, index, word_frequency):
    i = index

    for x in range(0, len(heap)):
        print('*     ', heap[x].key, ' hfreq: ', heap[x].frequency, ' wfreq: ', word_frequency[heap[x].key].frequency)

    while i > 0:
        parent_index = (i - 1) // 2
        print(heap[parent_index].key, heap[i].key, heap[parent_index].frequency, ' > ', heap[i].frequency)
        if heap[parent_index].frequency > heap[i].frequency:
            parent = heap[parent_index]
            heap[parent_index] = heap[i]
            heap[i] = parent

            word_frequency[heap[parent_index].key].index = parent_index
            word_frequency[heap[i].key].index = i

            i = parent_index
        else:
            i -= 1

    for i in range(0, len(heap)):
        print('     ', heap[i].key, word_frequency[heap[i].key].frequency)

    return heap


def add_heap(k, heap, word, word_frequency):
    if len(heap) < k:
        heap.append(HeapItem(word.key, word.frequency))
    else:
        if word.frequency > heap[0].frequency:
            if len(heap) == 1:
                removed = heap.pop()
                word_frequency[removed.key].index = -1
                heap.append(HeapItem(word.key, word.frequency))
            else:
                removed = heap[0]
                word_frequency[removed.key].index = -1
                heap[0] = heap[len(heap) - 1]
                moved = heap[0]
                word_frequency[moved.key].index = 0
                heap[len(heap) - 1] = HeapItem(word.key, word.frequency)
        else:
            return heap

    word_frequency[word.key].index = len(heap) - 1

    return heapify(heap, len(heap) - 1, word_frequency)

def build_del_dict(delimiters):
    dict = {}
    for delim in delimiters:
        if delim not in dict:
            dict[delim] = 1

    return dict