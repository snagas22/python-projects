"""
The solution code for construct binary tree from preorder and inorder traversal question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use recursion but faster
        # 62ms
        
        I = {j:i for i, j in enumerate(inorder)}
        def build(node, s, e):
            root = TreeNode(node)
            if s <= I[node] - 1:
                node_left = preorder.pop(0)
                root.left = build(node_left, s, I[node] - 1)
            if I[node] + 1 <= e:
                node_right = preorder.pop(0)
                root.right = build(node_right, I[node] + 1, e)
            return root
            
        return build(preorder.pop(0), 0, len(inorder) - 1)
        

    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use recursion
        # 296ms
        # edge case
        if not (preorder or inorder):
            return
        
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        
        root.left = self.buildTree1(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree1(preorder[idx+1:], inorder[idx+1:])
        
        return root