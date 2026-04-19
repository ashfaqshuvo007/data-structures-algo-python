from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0-5: 0,1,2,3,4,5
        # [0,2,4,5]
        #Using natural number series sum
        # sum = n * n + 1/ 2, where n in the series boundary in (0,n)
        n = len(nums)
        maxSum = n * (n + 1) // 2
        cSum = 0
        for n in nums:
            cSum += n
        return maxSum - cSum

if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 3]
    result = solution.missingNumber(nums)
    print(result)