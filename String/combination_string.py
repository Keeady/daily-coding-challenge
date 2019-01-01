class Combination:
    def __init__(self, str):
        self.str = str.strip()
        self.combinations = []

    def find_combination(self):
        str_arr = list(self.str)
        if len(str_arr) <= 1:
            return str_arr

        combinations = self.__generate_combinations(str_arr, [])

        print(combinations)
        for c in combinations:
            self.combinations.append(''.join(c))

        return self.combinations

    def __generate_combinations(self, str_arr, combinations):
        if len(str_arr) == 1:
            combinations.append(str_arr)
            return combinations

        char = str_arr[0]
        combinations = self.__generate_combinations(str_arr[1:], combinations)

        curr_combinations = []
        for c in combinations:
            c = c.copy()
            c.append(char)
            curr_combinations.append(c)

        combinations.extend(curr_combinations)
        combinations.append([char])

        return combinations