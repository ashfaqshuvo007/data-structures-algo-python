import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            time = 0

            for p in piles:
                time += math.ceil(p / k)
            
            if time <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([3, 6, 7, 11], 8))  # Output: 4
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Output: 30
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))  # Output: 23   

