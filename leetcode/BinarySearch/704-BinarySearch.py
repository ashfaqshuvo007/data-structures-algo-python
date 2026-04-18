from typing import List


class Solution:
    def binary_search(self, nums, l, r, target):
        if l > r:
            return -1

        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binary_search(nums, mid + 1, r, target)

        return self.binary_search(nums, l, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
    
if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    result = solution.search(nums, target)
    print(result)

    