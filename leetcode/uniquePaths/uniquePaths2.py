"""
The solution code for unique paths 2 question on leetcode.

Author: Shun Nagasaki

Problem:
A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique 
paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
"""

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        obstacleGrid[i][j] = 1
                        continue

                    if i == 0 or j == 0:
                        if i == 0:
                            obstacleGrid[i][j] = obstacleGrid[i][j-1]
                        else:
                            obstacleGrid[i][j] = obstacleGrid[i-1][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                        
        return obstacleGrid[-1][-1]