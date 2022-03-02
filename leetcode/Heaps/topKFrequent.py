"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from typing import List

from queue import PriorityQueue
from collections import defaultdict, Counter

class Solution:
    # better solution --> O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums).items()
        
        for num, freq in count:
            bucket[freq].append(num)
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]
    
    
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)
        q = PriorityQueue()
        ret = []
        
        for x in nums:
            table[x] += 1
        
        for key, val in table.items():
            q.put((-val, key))
        
        for _ in range(k):
            val, key = q.get()
            ret.append(key)
        
        return ret