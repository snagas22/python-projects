"""
The solution code for word break question on leetcode.

Author: Shun Nagasaki

Problem:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # use dynamic programming
        length = len(s)+1
        dp = [False] * length
        dp[0] = True
        
        for i in range(1, length):
            for word in wordDict:
                if dp[i-len(word)] and s[i-len(word):i] == word:
                    dp[i] = True
        
        return dp[-1]