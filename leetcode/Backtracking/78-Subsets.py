
#* Problem Statement


'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set 'must not contain duplicate subsets'. 
Return the solution in any order.

#?Constraints:
i) 1 <= nums.length <= 10
ii) -10 <= nums[i] <= 10
iii) All the numbers of nums are unique.

#? Examples:

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #? Approach 1 - Backtracking with recursive DFS 
        #? Time: O(n * 2^n) - Space: O(n) but with result add O(2^n)
        # res = []
        # subset = []

        # def dfs(idx):
        #     if idx >= len(nums):
        #         res.append(subset.copy())
        #         return
            
              #? Decision to include nums at idx
        #     subset.append(nums[idx])
        #     dfs(idx + 1)
              #? Decision to not include nums at idx
        #     subset.pop()
        #     dfs(idx + 1)

        # dfs(0)
        # return res

        #? Approach 2 - Iteration - Does not improve time and space but much simpler
        #? Time: O(n * 2^n) - Space: O(n) but with result add O(2^n)
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]
        
        return res
