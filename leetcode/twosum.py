"""
The solution code for two sum question on leetcode.

Author: Shun Nagasaki

Problem:
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to see which numbers exist in the input list
        numbers = {}
        # loop through the input list
        for i in range(len(nums)):
            # rest + current number = target
            rest = target - nums[i]
            # if rest is in the hashmap already, then you found the match
            if rest in numbers:
                # return the rest index and the current index
                return numbers[rest], i
            # if the current number is not in the hashmap,
            # then store it in the hashmap
            # {number: index}
            if nums[i] not in numbers:
                numbers[nums[i]] = i