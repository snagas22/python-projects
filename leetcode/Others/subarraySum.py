"""
The solution code for first unique character question on leetcode.

Author: Shun Nagasaki

Problem:
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prev = {0:1}
        presum = 0
        
        for x in nums:
            presum += x
            
            if presum-k in prev:
                total += prev[presum-k]
            
            if presum not in prev:
                prev[presum] = 1
            else:
                prev[presum] += 1
        
        return total
        