
#* 131 -  Palindrome Partitioning - MEDIUM

'''
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

 

#? Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

#?Example 2:

Input: s = "a"
Output: [["a"]]



'''
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        #* Approach 1 - Backtracking without pruning
        # def backtrack(i):
        #     if i >= len(s):
        #         res.append(part.copy())
        #         return

        #     for j in range(i, len(s)):
        #         if self.is_palindrome(s, i, j):
        #             part.append(s[i: j+ 1])
        #             backtrack(j + 1)
        #             part.pop()
        # backtrack(0)
        # return res

        #* Approach 2 - Backtracking with pruning - Only Valid palindromes
        def backtrack(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return
            if self.is_palindrome(s, j, i):
                part.append(s[j: i+ 1])
                backtrack(i + 1, i + 1)
                part.pop()

            backtrack(j, i + 1)
        backtrack(0, 0)
        return res

    def is_palindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False

            l, r = l + 1, r - 1

        return True