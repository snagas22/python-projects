"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.sub_rob(nums[:-1]), self.sub_rob(nums[1:]))
    
    def sub_rob(self, nums):
        prev1 = prev2 = 0
        for x in nums:
            tmp = prev1
            prev1, prev2 = max(prev2 + x, prev1), tmp
        return prev1