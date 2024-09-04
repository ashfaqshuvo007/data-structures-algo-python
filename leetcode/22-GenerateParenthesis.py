'''
Leetcode - 22 MEDIUM
You are given an integer n. Return all well-formed parentheses strings that you can 
generate with n pairs of parentheses.

'''

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Only add open parenthesis if open < n
        

        stack = []
        result = []


        def backtrack(openN, closedN):
            # Valid and we stop IIF open === close === n
            if openN == closedN == n:
                result.append("".join(stack))
            
            # Only add open parenthesis if open < n
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            
            # Only add close parenthesis if Close < open
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)

        return result


if __name__ == '__main__':
    sln = Solution()
    print(sln.generateParenthesis(5))