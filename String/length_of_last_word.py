def find_length_of_last_word(input):
    input = input.strip()

    i = len(input) - 1

    while i >= 0:
        if input[i] == ' ':
            break
        i -= 1

    return len(input) - i - 1