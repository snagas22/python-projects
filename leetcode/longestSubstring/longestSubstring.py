"""
The solution code for longest substring without
repeating characters question on leetcode.

Author: Shun Nagasaki

Problem:
Given a string s, find the length of the longest substring 
without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 1
        ans = ''
        length = 0
        # iterate through the input string
        for i in range(len(s)):
            # if the current string has the s[i] in it,
            # then shift the start index to the right of
            # where that letter is
            if s[i] in ans:
                start = s.index(s[i], start) + 1
            # set ans to the new substring
            ans = s[start:end]
            # if the new substring is longer
            # then update the max length
            if len(ans) >= length :
                length = len(ans)
            # increment the right pointer of the substring
            end += 1

        return length

# one of the solutions from the leetcode Discussion page
class Solution_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by 
            moving right pointer
            """
            if s[r] not in seen:
                output = max(output,r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output