## Pairs with difference
Find all pairs that have a specified difference among a set  of n integers.

## Merge ranges
merge ranges. given [2, 5] [4, 8] [10, 12], return [2, 8] [10, 12]  

## Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet
 that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an
 array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an
  empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to 
return the first one you encounter (considering the results are sorted).

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)

## Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].
Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

## Find the duplicate number 
Given an array nums containing n + 1 integers where each integer is between 1 and 
n (inclusive), prove that at least one duplicate number must exist. Assume that there 
is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
