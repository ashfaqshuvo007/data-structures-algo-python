
#* 695 - Max Area of Island - MEDIUM

'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

#? Example 1:
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

#? Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

'''

from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Approach: Recursive DFS and marking visted cells
        #Time & Space: O(m * n) ; m and n are no of rows and cols 
        ROWS = len(grid)
        COLS = len(grid[0])

        maxArea = 0

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return 0
            grid[r][c] = -1
            return 1 + (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea