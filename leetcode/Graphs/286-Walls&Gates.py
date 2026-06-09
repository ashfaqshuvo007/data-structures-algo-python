
#* Problem: Similar to Leetcode: 286 - WALLS & GATES - MEDIUM

'''
You are given a m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. 
If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}

'''
from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])

        def addCell(r, c):
            # Since we are doing BFS r == ROWS satisfying the out of bound check
            # instead of r >= ROWS we use in case of DFS
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == -1):
                return

            visited.add((r, c))
            queue.append([r, c])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visited.add((row, col))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
