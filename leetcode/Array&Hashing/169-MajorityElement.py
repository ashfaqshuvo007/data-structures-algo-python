
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            count[num] += 1

            if count[num] > maxCount:
                res = num
                maxCount = count[num]

        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3,2,3])) # 3
    print(s.majorityElement([2,2,1,1,1,2,2])) # 2   