"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
nums = [2,7,11,15]
target = 9
class Solution:
    def twoSum(self, nums, target):
        visited = {} 
        for i, n in enumerate(nums):
            if (target - nums[i]) in visited: 
                return [visited[target - nums[i]], i] 
            visited[n] = i
        return 

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums, target))

        