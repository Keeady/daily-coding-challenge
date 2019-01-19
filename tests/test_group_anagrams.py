from String import group_anagrams


def test_group_anagrams():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groups = group_anagrams.group_anagrams(words)

    assert len(groups) == len([["ate","eat","tea"], ["nat","tan"], ["bat"]])