from String import remove_specified_chars


def test_remove_chars():
    str = "Battle of the Vowels: Hawaii vs. Grozny"
    remove = "aeiou"
    assert remove_specified_chars.remove_specified_chars(str, remove) == "Bttl f th Vwls: Hw vs. Grzny"


def test_remove_all_chars():
    str = "velona e velona e"
    remove = "velona"
    assert remove_specified_chars.remove_specified_chars(str, remove) == ""

def test_remove_long_chars():
    str = "velona"
    remove = "xyzeonlvaithg"
    assert remove_specified_chars.remove_specified_chars(str, remove) == ""

def test_remove_same_chars():
    str = "velona"
    remove = "velona"
    assert remove_specified_chars.remove_specified_chars(str, remove) == ""
