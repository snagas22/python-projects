"""
The solution code for first unique character question on leetcode.

Author: Shun Nagasaki

Problem:
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
"""

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        
        while low < high:
            mid = (low+high)//2
            
            curr = 0
            num_ships = 1
            for w in weights:
                curr += w
                if curr > mid:
                    curr = w
                    num_ships += 1
            
            
            if num_ships > days:
                low = mid+1
            else:
                high = mid
        
        return low