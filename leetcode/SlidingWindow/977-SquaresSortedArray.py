from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ## Complexity - O(n) / O(n)
        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     res[i] = nums[i] * nums[i]
        
        # return sorted(res)

        ## Second Approch - Sliding Window
        l = 0
        r = len(nums) - 1
        res = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [-4, -1, 0, 3, 10]
    result = solution.sortedSquares(nums)
    print(result)
    
