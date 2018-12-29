from String import reverse_string


def test_reverse_words():
    str = "piglet quantum"
    assert reverse_string.reverse_words(str) == "quantum piglet"
