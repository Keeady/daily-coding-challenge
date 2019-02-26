import heapq


def lookup_number(num, name_directory, phone_directory):
    names = name_directory[str(num)]

    results = {}

    for name in names:
        results[name] = phone_directory[name]

    return results

def build_name_directory(name_list):
    key_pad = {
        2: ['A','B','C'],
        3: ['D','E','F'],
        4: ['G','H','I'],
        5: ['J','K','L'],
        6: ['M','N','O'],
        7: ['P','R','S'],
        8: ['T','U','V'],
        9: ['W','X','Y']
    }

    phone_directory = {}
    name_directory = {}

    letters_to_key = build_letter_lookup(key_pad)

    for entry in name_list:
        (name, phone) = entry.split(' ')

        # same name, diff phone
        if name not in phone_directory:
            phone_directory[name] = []

        phone_directory[name].append(phone)

        sign = build_name_signature(name, letters_to_key)
        if sign not in name_directory:
            name_directory[sign] = []

        heapq.heappush(name_directory[sign], name)

    return (name_directory, phone_directory)


def build_name_signature(name, letters_to_key):
    signature = []
    for char in name:
        signature.append(letters_to_key[char.upper()])

    return ''.join(signature)


def build_letter_lookup(key_pad):
    letters_to_key = {}

    for key in key_pad:
        letters = key_pad[key]

        for letter in letters:
            letters_to_key[letter] = str(key)

    return letters_to_key
