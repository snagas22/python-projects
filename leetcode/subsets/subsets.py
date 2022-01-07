"""
The solution code for subsets question on leetcode.

Author: Shun Nagasaki

Problem:
Given an integer array nums of unique elements, return 
all possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums, [], ret)
        return ret
    
    
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], ret)