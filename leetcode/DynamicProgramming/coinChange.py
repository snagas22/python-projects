"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        if amount == 0:
            return 0
        
        queue = [(0, 0)]
        visited = set()
        
        while queue:
            curr, num = queue.pop(0)
            for coin in coins:
                if curr + coin in visited:
                    continue
                if curr + coin == amount:
                    return num + 1
                if curr + coin < amount:
                    queue.append((curr+coin, num+1))
                    visited.add(curr+coin)
        
        return -1