"""
The solution code for binary tree zigzag level order traversal question on leetcode.

Author: Shun Nagasaki

Problem:
Given the root of a binary tree, return the zigzag level order traversal 
of its nodes' values. (i.e., from left to right, then right to left for the 
next level and alternate between).
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l_to_r = 1
        
        ret = []
        queue = [root]
        
        while queue:
            length = len(queue)
            level = []
            
            for i in range(length):
                curr = queue.pop(0)
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                
            if l_to_r == -1:
                level = level[::-1]
            if level:
                ret.append(level)
            l_to_r *= -1
            
        return ret
            