from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) //2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l]

if __name__ == "__main__":
    solution = Solution()
    nums = [3,4,5,1,2]
    result = solution.findMin(nums)
    print(result)
    