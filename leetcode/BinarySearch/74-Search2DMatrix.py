from typing import List

#? MY Solution - O(m log n) where m is the number of rows and n is the number of columns
class Solution:
    def binary_search(self, row, t):
        l = 0
        r = len(row) - 1
        while l <= r:
            m = (l + r) // 2

            if t == row[m]:
                return True
            
            if row[m] < t:
                l = m + 1
            else:
                r = m - 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if (self.binary_search(row, target)):
                return self.binary_search(row, target)
        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)) # return True
    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)) # return False
    