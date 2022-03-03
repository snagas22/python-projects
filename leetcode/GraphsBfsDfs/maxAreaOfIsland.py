"""
The solution code for first unique character question on leetcode.

Author: Shun Nagasaki

Problem:
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    curr = self.dfs(grid, i, j)
                    area = max(area, curr)
                    
        return area
    
    
    def dfs(self,grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or not grid[i][j]:
            return 0
    
        grid[i][j] = 0
        
        return 1 + self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1)