"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for nonzero in range(len(nums)):
            if nums[nonzero] != 0 and nums[zero] == 0:
                nums[nonzero], nums[zero] = nums[zero], nums[nonzero]
            
            if nums[zero] != 0:
                zero += 1