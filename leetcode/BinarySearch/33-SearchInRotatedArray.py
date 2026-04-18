from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            #left sorted Portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #Right sorted Portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

if __name__ == "__main__":
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = solution.search(nums, target)
    print(result)

    