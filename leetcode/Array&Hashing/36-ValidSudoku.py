'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

'''

#* Hash Set (One Pass) - Intuition

# * Instead of checking rows, columns, and 3×3 boxes separately, we can validate the entire Sudoku board in one single pass.

# * For each cell, we check whether the digit has already appeared in:
# *   - the same row
# *   - the same column
# *   - the same 3×3 box

# * We track these using three hash sets:

# * rows[r] keeps digits seen in row r
# * cols[c] keeps digits seen in column c
# * squares[(r // 3, c // 3)] keeps digits in the 3×3 box
# * If a digit appears again in any of these places, the board is invalid.

from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # if current position in empty
                if board[r][c] == ".":
                    continue
                # the current positon value is already visited
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]): # this check is where the magic happens
                    return False
                # Add current value to matrix if not seen
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        # Finally if no duplicate return
        return True
    
if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    print(solution.isValidSudoku(board))

