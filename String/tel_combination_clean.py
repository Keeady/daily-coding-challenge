from String import telephone_util


def get_char_key(key, place):
    keys = {
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

    if key not in keys or place > 3 or place < 1:
        return ''

    letters = keys[key]

    if len(letters) == 0:
        return ''

    return letters[place - 1]

def gen_tel_combination(digits, i, combinations, c):
    if i >= 7:
        combinations.append(''.join(c))
        return combinations

    for place in range(1, 4):
        letter = get_char_key(digits[i], place)
        if len(letter) == 0:
            c[i] = str(digits[i])
        else:
            c[i] = letter

        gen_tel_combination(digits, i + 1, combinations, c)

        if digits[i] == 1 or digits[i] == 0:
            return combinations

    return combinations