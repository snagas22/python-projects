"""
The solution code for generate parentheses question on leetcode.

Author: Shun Nagasaki

Problem:
Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # depth first search
        self.dfs(ans, '', n, n)
        return ans
    
    def dfs(self, ans, path, left, right):
        # base cases:
        # 1. if remaining left side is greater, there are more
        #    left brackets remaining than right brackets. This means
        #    you can't make valid ones because left always precedes right
        #    brackets.
        # 2. if remaining left is less than 0, go back to the previous call
        # 3. same for the remaining right
        if left > right or left < 0 or right < 0:
            return
        # if the remaining left and right are 0, it means it used up 
        # left and right correctly, so add it to the answer list
        if left == 0 and right == 0:
            ans.append(path)
            return
        # recursive call with one less left bracket
        self.dfs(ans, path+'(', left-1, right)
        # recursive call with one less right bracket
        self.dfs(ans, path+')', left, right-1)