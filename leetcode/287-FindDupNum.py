from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return nums[i]
            else:
                visited.add(nums[i])

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    result = solution.findDuplicate(nums)
    print(result)
    