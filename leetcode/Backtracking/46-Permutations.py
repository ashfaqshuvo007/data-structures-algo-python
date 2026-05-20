
#* Problem Statement
#* 46. Permutations - HARD
'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

#? Examples:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]

'''

from typing import List
class Solution:
    # Approach 1 - Recursion tackling new permutations array - O(n!∗n^2)/ O(n!∗n^2)
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base Case
        if len(nums) == 0:
            return [[]]

        # calculate Permutaions without the first element
        perms = self.permute(nums[1:])
        res = []

        # Loop through each permutation and the 1st element at different positons
        for p in perms:
            for i in range(
                len(p) + 1
            ):  # len(p) + 1 coz, we might add at the last place as well
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res

    # Approach 2 - Backtracking In-place SWAP - O(n!∗n)/ O(n!∗n)
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     self.res = []
    #     self.backtrack(nums, 0)
    #     return self.res

    # def backtrack(self, nums: List[int], idx: int):
    #     if idx == len(nums):
    #         self.res.append(nums[:])
    #         return
    #     for i in range(idx, len(nums)):
    #         nums[idx], nums[i] = nums[i], nums[idx]
    #         self.backtrack(nums, idx + 1)
    #         nums[idx], nums[i] = nums[i], nums[idx]