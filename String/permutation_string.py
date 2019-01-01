def perm_rec(str):
    permutations = []
    str_arr = list(str)

    if len(str_arr) == 0:
        return []

    perms = __gen_rec_perm(str_arr)

    for p in perms:
        permutations.append(''.join(p))

    return permutations

def __gen_rec_perm(str_arr):
    if len(str_arr) == 1:
        return [str_arr]

    char = str_arr[0]
    perms = __gen_rec_perm(str_arr[1:])
    perms = __insert_into_perms(char, perms)

    return perms

def __insert_into_perms(char, perms):
    perm_list = []
    for perm_str in perms:
        insert_index = 0

        while insert_index <= len(perm_str):
            perm = __generate(perm_str.copy(), char, insert_index)

            perm_list.append(perm)

            insert_index += 1
    return perm_list

def __generate(str_arr, char, insert_index):
    str_arr.insert(insert_index, char)
    return str_arr
