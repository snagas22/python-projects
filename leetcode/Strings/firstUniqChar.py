"""
The solution code for first unique character question on leetcode.

Author: Shun Nagasaki

Problem:
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
            
        return -1