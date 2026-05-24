
#* 40- Combination Sum II - MEDIUM

'''
#? Problem Statement:

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

#? Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

#? Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]


#?Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]



'''




from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #* Approach 1: Backtracking - Time: O(n*2^n) Space: O(n)
        # res = []
        # candidates.sort()

        # def dfs(idx, path, total):
        #     if total == target:
        #         res.append(path.copy())
        #         return

        #     if idx >= len(candidates) or total > target:
        #         return

        #     path.append(candidates[idx])
        #     dfs(idx + 1, path, total + candidates[idx])
        #     path.pop()

        #     while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
        #         idx += 1

        #     dfs(idx+1, path, total)

        # dfs(0, [], 0)
        # return res

        #* Approach 2: Backtracking - Time: O(n*2^n) Space: O(n)
        #* With path pruning and sorting
        res = []
        candidates.sort()

        def dfs(idx, path, curSum):
            if curSum == target:
                res.append(path.copy())
                return
            
            for j in range(idx, len(candidates)):
                if j > idx and candidates[j] == candidates[j - 1]:
                    continue
                
                if curSum + candidates[j] > target:
                    return
                
                path.append(candidates[j])
                dfs(j + 1, path, curSum + candidates[j])
                path.pop()

        dfs(0, [], 0)
        return res