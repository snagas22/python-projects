"""
The solution code for string to integer question on leetcode.

Author: Shun Nagasaki

Problem:
Implement the myAtoi(string s) function, which converts a string to a 
32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) 
is '-' or '+'. Read this character in if it is either. This determines 
if the final result is negative or positive respectively. Assume the result 
is positive if neither is present.
3. Read in next the characters until the next non-digit character or the 
end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
If no digits were read, then the integer is 0. Change the sign as necessary 
(from step 2).
5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
then clamp the integer so that it remains in the range. Specifically, 
integers less than -231 should be clamped to -231, and integers greater than 
231 - 1 should be clamped to 231 - 1.
6. Return the integer as the final result.

Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the 
rest of the string after the digits.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        neg = False
        ans = ''
        # edge case 1
        if s is None or len(s) == 0:
            return 0
        # removes leading whitespaces
        s = s.strip()
        # if + or - is present and there is at least
        # one character after that, then check whether
        # the value is positive or negative
        if len(s) > 1 and (s[0] == '+' or s[0] == '-'):
            if s[0] == '+': 
                neg = False
            else:
                neg = True
            s = s[1:]
        # len(s) should be at least 1 here.
        # if the next character is not a number,
        # return 0
        if len(s) == 0 or not s[0].isnumeric():
            return 0
        
        # loop through the rest of the string while
        # the current character is numeric
        i = 0
        while i < len(s) and s[i].isnumeric():
            ans += s[i]
            i += 1
        # convert to integer
        ans = int(ans)
        # if positive: return as is or 2**31-1 if number is too big
        # if negative: return -1*ans or -2**31 if number is too small
        return min(ans, 2**31-1) if not neg else max(-1*ans, -2**31)