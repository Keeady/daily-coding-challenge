# nums1 is long enough to fit nums2
# true length of nums1 = len(nums1) - len(nums2)
# insert from the end of nums1
# compare nums1 and nums2
# nums1 starting at the true length - 1 index
# insert the smallest of nums1 and nums2 then increment
# until all of nums2 are copied or we reach the start of nums1
# in which copy all remaining nums2 into nums1

# [1,2,2,3,5,6]
# [2,5,6]
def merge_sorted_array(nums1, length1, nums2, length2):
    insert_index = len(nums1) - 1 #5
    nums1_index = length1 - 1 #2
    nums2_index = length2 - 1 #2

    if length1 == 0 and length2 == 0:
        return nums1

    while nums1_index >= 0 and nums2_index >= 0:  #0, #-1
        if nums2[nums2_index] > nums1[nums1_index]:
            nums1[insert_index] = nums2[nums2_index]
            nums2_index -= 1
        else:
            nums1[insert_index] = nums1[nums1_index]
            nums1_index -= 1

        insert_index -= 1 #1

    if nums2_index >= 0:
        copy_arr(nums1, insert_index, nums2, nums2_index)

    return nums1


def copy_arr(target, target_index, source, source_index):
    while source_index >= 0:
        target[target_index] = source[source_index]
        target_index -= 1
        source_index -= 1

    return target