"""
The solution code for delete duplicates question on leetcode.

Author: Shun Nagasaki

Problem:
Given the head of a sorted linked list, delete all nodes that have 
duplicate numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre, curr = dummy, head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next
        
        return dummy.next
        
            