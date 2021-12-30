"""
The solution code for search insert position question on leetcode.

Author: Shun Nagasaki

Problem:
Given a sorted array of distinct integers and a target value, return 
the index if the target is found. If not, return the index where it would 
be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        
        left, right = 0, len(nums) - 1
        mid = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
        return left