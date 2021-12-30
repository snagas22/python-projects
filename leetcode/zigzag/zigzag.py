"""
The solution code for zigzag conversion question on leetcode.

Author: Shun Nagasaki

Problem:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a 
fixed font for better legibility):

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = 1
        # hashmap to store strings for each row
        # key: nth row, value: string
        rows = {}
        up = True
        ans = ''
        # edge case when number of rows is 1
        # Return the input string as is
        if numRows == 1:
            return s
        # edge case 2
        # if the length of the input string is shorter than
        # the input numRows, return the original string
        if len(s) < numRows:
            return s
        # loop through the input string to see
        # which row each letter belongs to
        for x in s:
            if row not in rows:
                rows[row] = x
            else:
                rows[row] += x
            # if row reaches the bottom of the zigzag,
            # start decrementing it
            if row == numRows:
                up = False
            # if row reaches the top of zigzag,
            # start incrementing it
            if row == 1:
                up = True
            
            if up:  row += 1
            if not up: row -= 1
        # loop through the hashmap to concatenate
        # all the strings together
        for i in range(1, numRows+1):
            ans += rows[i]
        
        return ans