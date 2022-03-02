"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.
"""

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        h = []
        visited = set((0, 0))
        
        heapq.heappush(h, (nums1[0] + nums2[0], 0, 0))
        
        while len(ans) < k and h:
            _, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])
            
            if i+1 < n1 and (i+1, j) not in visited:
                heapq.heappush(h, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
                
            if j+1 < n2 and (i, j+1) not in visited:
                heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))
        
        return ans
        