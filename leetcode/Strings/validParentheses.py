"""
The solution code for valid parentheses question on leetcode.

Author: Shun Nagasaki

Problem:
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # loop through the string
        for bracket in s:
            # if it's one of the left side bracket,
            # append the corresponding right side of it
            # to the stack list
            if bracket == '(':
                stack.append(')')
            elif bracket == '[':
                stack.append(']')
            elif bracket == '{':
                stack.append('}')
            else:
                # if not the left side, check the stack list
                # If the stack is empty, return False because
                # there's a mismatch.
                # Pop the last element in the stack and check
                # if it's the same as the current bracket.
                # Return False if it doesn't match
                if len(stack) > 0:
                    closing = stack.pop()
                    if closing != bracket:
                        return False
                else:
                    return False
        # return True if the stack is empty, meaning all brackets
        # match up. If not, return False
        return True if len(stack) == 0 else False