"""
The solution code for delete duplicates question on leetcode.

Author: Shun Nagasaki

Problem:
Given the head of a sorted linked list, delete all duplicates such that 
each element appears only once. Return the linked list sorted as well.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
            
        return head