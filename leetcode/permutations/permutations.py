"""
The solution code for string to integer question on leetcode.

Author: Shun Nagasaki

Problem:
Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # simple edge case
        if not nums:
            return []
        
        ret = []
        # backtracking with dfs approach
        def dfs(nums, path, ret):
            # if the remaining is empty, add the path to the answer list
            if not nums:
                ret.append(path)
            # loop through nums list for each call to dfs
            for i in range(len(nums)):
                # nums[:i]+nums[i+1:] is making a list with nums[i] being
                # extracted from nums. It's essentially just nums list without
                # the nums[i] value in it
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], ret)
        
        dfs(nums, [], ret)
        return ret