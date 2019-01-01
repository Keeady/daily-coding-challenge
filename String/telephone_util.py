class telephone_util:
    def __init__(self):
        self.keys = {
            0: [],
            1: [],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y']
        }

    def get_char_key(self, key, place):
        if key not in self.keys or place > 3 or place < 1:
            return ''

        letters = self.keys[key]

        if len(letters) == 0:
            return ''

        return letters[place - 1]