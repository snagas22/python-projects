"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ans = float("inf")
        left = 0
        total = 0
        
        for right in range(len(nums)):
            total += nums[right]
            
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
            
        return ans if ans != float("inf") else 0