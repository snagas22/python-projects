"""
The solution code for next permutation question on leetcode.

Author: Shun Nagasaki

Problem:
Implement next permutation, which rearranges numbers into the 
lexicographically next greater permutation of numbers.

If such an arrangement is impossible, it must rearrange it to the lowest 
possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Note: use the idea of two pointers.
        """
        # two pointers i, j
        n = len(nums)
        i = j = n - 1
        # starting from the back of the list,
        # if i > 0 and the number to the left is
        # >= than the current one, move i pointer 
        # to the left
        while i and nums[i-1] >= nums[i]:
            i -= 1
        # starting from the back of the list,
        # if j > i and i > 0 and the number at the j pointer
        # is <= the number to the left of the i pointer,
        # then move j pointer to the left
        while j > i and i and nums[j] <= nums[i-1]:
            j -= 1
        # swap numbers at i-1 pointer and j pointer
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        j = n - 1
        # starting from the back again,
        # while j pointer is still greater than the i pointer,
        # swap numbers at i and j pointers and bring them in by 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        