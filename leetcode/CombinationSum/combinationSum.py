"""
The solution code for combination sum question on leetcode.

Author: Shun Nagasaki

Problem:
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen 
numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen 
numbers is different.

It is guaranteed that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # edge case
        if not candidates:
            return []
        
        ret = []
        
        def dfs(candidates, target, path, ret):
            # if the sum goes over the target, return nothing and move onto the next search
            if target < 0:
                return
            # if the sum == target, add the path to the answer list and return
            if target == 0:
                ret.append(path)
            # try all possible combinations by backtracking
            # iterate through the remainding candidates list
            for i in range(len(candidates)):
                dfs(candidates[i:], target-candidates[i], path+[candidates[i]], ret)
        
        dfs(candidates, target, [], ret)
        return ret