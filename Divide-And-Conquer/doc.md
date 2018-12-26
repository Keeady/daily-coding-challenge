## Maximum-subarray problem
- Brute force: try every pair of buy and sell dates where buy
date precedes sell date O(n2)
- Divide and Conquer: find the sequence of days where the 
net change between the first day to last is maximum
    - Divide the array into two sub-arrays of equal size
    - Find the mid point
    - The maximum sub-array must lie between low and mid, mid and high, or
    across low-mid-high
    
 ## Matrix Multiplication
 - Naive Approach: multiply each rows to each columns O(n3)
 _ Divide and Conquer:
 
 ## Maximum Size Subarray Sum Equals k
 Given an array of numbers and a target value k, find the maximum length of a subarray
  that sums to k. If there isn't one, return 0 instead.
  Given nums = [1, -1, 5, -2, 3], k = 3, return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
  Given nums = [-2, -1, 2, 1], k = 1, return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

