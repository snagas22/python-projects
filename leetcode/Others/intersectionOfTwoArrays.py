"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = set(nums1) & set(nums2)
        return list(ret)