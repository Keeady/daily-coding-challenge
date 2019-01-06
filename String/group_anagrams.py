import collections
def group_anagrams(words):
    anagram_dict = {}

    for w in words:
        w_list = list(w)
        w_list.sort()
        w_sorted = ''.join(w_list)
        if w_sorted in anagram_dict:
            curr_group = anagram_dict[w_sorted]

        else:
            curr_group = []

        curr_group.append(w)
        anagram_dict[w_sorted] = curr_group

    return list(anagram_dict.values())