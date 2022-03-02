"""
The solution code for is subsequence question on leetcode.

Author: Shun Nagasaki

Problem:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = count = 0
        tlen = len(t)
        slen = len(s)
        
        for i in range(slen):
            while j < tlen and s[i] != t[j]:
                j += 1
            
            if j >= tlen:
                return False
            
            if s[i] == t[j]:
                j += 1
                count += 1
            
        if count == slen:
            return True
        return False