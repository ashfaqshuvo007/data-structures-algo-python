
#* 17. Letter combinations of a Phone number

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#? Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

#? Example 2:

Input: digits = "2"
Output: ["a","b","c"]


'''
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        com = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(i, curCombo):
            if len(digits) == len(curCombo):
                res.append(curCombo)
                return

            for c in com[digits[i]]:
                backtrack(i + 1, curCombo + c)

        if digits:
            backtrack(0, "")

        return res