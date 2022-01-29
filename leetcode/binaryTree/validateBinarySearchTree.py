"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""

from math import inf
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)
    
    
    def dfs(self, root, left=-inf, right=inf):
        if not root:
            return True
        
        if not (left < root.val < right):
            return False

        return self.dfs(root.left, left, root.val) and self.dfs(root.right, root.val, right)