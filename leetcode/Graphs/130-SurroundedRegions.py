
#* 130. Sourrounded Regions - MEDIUM

'''
You are given an m x n matrix board containing letters 'X' and 'O', 
capture regions that are surrounded:

-  Connect: A cell is connected to adjacent cells horizontally or vertically.
-  Region: To form a region connect every 'O' cell.
-  Surround: A region is surrounded if none of the 'O' cells in that region are 
    on the edge of the board. Such regions are completely enclosed by 'X' cells.

To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. 
You do not need to return anything.

#? Example: 1
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation: The bottom 'O' region is not captured because it touches 
the edge of the board, so it cannot be surrounded.

#? Example 2:

Input: board = [["X"]]
Output: [["X"]]

'''
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Capture recursive
        def capture(r, c):
            # check if unbound
            if min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return

            # We use the current cell, mark for not repeating
            board[r][c] = "#"
            # run capture on all adjacent cells
            for dx, dy in directions:
                capture(r + dx, c + dy)

        # capture all edge cells
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        # Traverse finally to check if all cells marked
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"