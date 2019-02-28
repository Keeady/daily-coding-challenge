# sort the arrays
# think about merging 2 sorted arrays
import sys


def find_smallest_diff(arrA, arrB):
    arrA.sort()
    arrB.sort()

    left = 0
    right = 0

    min_diff = sys.maxsize

    while left < len(arrA) and right < len(arrB):
        diff = abs(arrA[left] - arrB[right])

        if diff < min_diff:
            min_diff = diff

        if arrA[left] <= arrB[right]:
            left += 1
        else:
            right += 1

    return min_diff
