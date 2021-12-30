"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
"""

class Solution:
    def myPow(self, x:float, n:int) -> float:
        # recursive answer
        # base case
        if not n:
            return 1
        # if negative, flip x and make n positive
        if n < 0:
            x = 1/x
            n *= -1
        # x*x if n is negative after /2 an if not, multiply by an extra x to make
        # up for the odd number
        return self.myPow(x*x, n//2) if n % 2 == 0 else x*self.myPow(x*x, n//2)
    
    # these two are using python's builtin functionalities
    def myPow1(self, x: float, n: int) -> float:
        return pow(x, n)
    
    def myPow2(self, x: float, n: int) -> float:
        return x ** n