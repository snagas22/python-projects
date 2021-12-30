"""
The solution code for group anagrams question on leetcode.

Author: Shun Nagasaki

Problem:
Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # edge case
        if not strs:
            return []
        
        words = {}
        
        # loop through the input string list
        for s in strs:
            # sort the string alphabetically
            s_sort = "".join(sorted(s))
            # if the sorted word is in the map
            # add it to its value
            if s_sort in words:
                words[s_sort].append(s)
            # if seen for the first time,
            # create the key val pair with the original
            # string in a list
            else:
                words[s_sort] = [s]
        
        return words.values()