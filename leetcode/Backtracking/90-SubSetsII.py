
#* 90 - Subsets II - MEDIUM
''' 
#? Problem Statement
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

#? Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

#? Example 2:

Input: nums = [0]
Output: [[],[0]]

'''

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ##* APPROACH 1:  Backtracking and check for duplicating before backtrack
        ##*  Time: O(n * n^2) - Space: O(n) and O(2^n)

        # res = []
        # subset = []
        # nums.sort()

        # def backtrack(idx):
        #     if idx == len(nums):
        #         res.append(subset.copy())
        #         return

        #     # Use current num
        #     subset.append(nums[idx])
        #     backtrack(idx + 1)
        #     # Skip current num
        #     subset.pop()
        #     # Checking and discarding duplicates
        #     while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
        #         idx += 1

        #     backtrack(idx + 1)

        # backtrack(0)
        # return res

        ##* APPROACH 2:  Backtracking with graceful pruning
        ##*  Time: O(n * n^2) - Space: O(n) and O(2^n)

        res = []
        nums.sort()

        def backtrack(idx, subset):
            #* this is a change, For every backtrack we add current subset to result, 
            #* Not checking if it is the end of the input
            res.append(subset.copy()) 
            

            for j in range(idx, len(nums)):
                if j > idx and nums[j] == nums[j - 1]:
                    continue

                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res