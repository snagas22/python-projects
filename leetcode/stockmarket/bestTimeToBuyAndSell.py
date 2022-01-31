"""
The solution code for pow question on leetcode (done recursively).

Author: Shun Nagasaki

Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - buy_price
            
            if profit > max_profit:
                max_profit = profit
            
            if prices[i] < buy_price:
                buy_price = prices[i]
        
        return max_profit