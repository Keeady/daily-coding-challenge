# use left, right window
# 
def find_first_occurrence_substr(haystack, needle):
    if len(needle) == 0:
        return 0

    length = len(haystack)
    left = 0
    right = len(needle)

    while right - 1 < length:
        if haystack[left:right] == needle:
            return left

        left += 1
        right += 1

    return -1