"""
The solution code for first unique character question on leetcode.

Author: Shun Nagasaki

Problem:
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        half_mark = 2 ** (n-2) # or 2 ** (n-1) // 2
        
        if k <= half_mark:
            return self.kthGrammar(n-1, k)
        else:
            second_half = self.kthGrammar(n-1, k-half_mark)
            if second_half == 0:
                return 1
            else:
                return 0
            