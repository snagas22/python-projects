"""
The solution code for add two numbers question on leetcode.

Author: Shun Nagasaki

Problem:
You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers 
and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # node for adding up the answer
        ans = ListNode()
        # node to return at the end
        head = ans
        # temporary to store carry (ex. 14 --> tmp = 1)
        tmp = 0
        # loops while one of the nodes still exists
        while l1 or l2:
            one = two = 0
            # if there is a still l1 node --> one stores l1 val
            # same for two and l2
            if l1:
                one = l1.val
            if l2:
                two = l2.val
            # adding up the vals for the current node
            curr = one + two + tmp
            # the remainder becomes the val for this node
            ans.next = ListNode(curr%10)
            # this is the carry
            tmp = curr//10
            # advance to next node
            ans = ans.next
            # advance l1 and l2 to next node if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # at the end, if the carry still exists,
        # add another node with the val = carry
        if tmp > 0:
            ans.next = ListNode(tmp)
        # return head (start of the answer linked list)
        return head.next