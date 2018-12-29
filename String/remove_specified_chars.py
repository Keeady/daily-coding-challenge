def remove_specified_chars(str, remove):
    if len(remove) == 0 or len(str) == 0:
        return str

    output = []
    remove_chars = {}
    for char in remove:
        remove_chars[char] = True

    for char in str:
        if char not in remove_chars:
            output.append(char)

    return ''.join(output).strip()
