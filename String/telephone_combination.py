from String import telephone_util

class telephone_number:
    def __init__(self, util: telephone_util.telephone_util, digits):
        self.util = util
        self.digits = digits
        self.combinations = []

    def print_words(self):
        if len(self.digits) != 7:
            return []

        combinations = self.__gen_combinations(self.digits)
        for c in combinations:
            self.combinations.append(''.join(c))

        return self.combinations

    def __gen_combinations(self, digits):
        if len(digits) == 1:
            letters = self.__translate_digit(digits[0])
            letter_comb = []

            for letter in letters:
                letter_comb.append([letter])

            return letter_comb

        digit = digits[0]
        combinations = self.__gen_combinations(digits[1:])
        letters = self.__translate_digit(digit)

        curr_combinations = []
        for letter in letters:
            for c in combinations:
                curr = c.copy()
                curr.insert(0, letter)
                curr_combinations.append(curr)

        return curr_combinations

    def __translate_digit(self, digit):
        letters = []
        i = 1
        while i <= 3:
            letter = self.util.get_char_key(digit, i)
            if len(letter) > 0:
                letters.append(letter)
            i += 1

        if len(letters) == 0:
            letters.append(str(digit))

        return letters