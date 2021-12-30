"""
The solution code for maximum sub array question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and 
return its sum.

A subarray is a contiguous part of an array.
"""

from itertools import accumulate
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(beg, end):
            if beg + 1 == end: return nums[beg]
            mid = (beg + end)//2
            sum_1 = helper(beg, mid)
            sum_2 = helper(mid, end)
            right = max(accumulate(nums[beg:mid][::-1]))
            left  = max(accumulate(nums[mid:end]))
            return max(sum_1, sum_2, left + right)

        return helper(0, len(nums))
    
    
    def maxSubArray1(self, nums: List[int]) -> int:
        curr = maxNum = nums[0]
        
        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i] + curr)
            maxNum = max(maxNum, curr)
        
        return maxNum
    
    
    def maxSubArray2(self, nums: List[int]) -> int:
        return max(accumulate(nums, lambda x, y: max(x+y, y)))