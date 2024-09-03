'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

i. Open brackets must be closed by the same type of brackets.
ii. Open brackets must be closed in the correct order.
iii. Every close bracket has a corresponding open bracket of 
the same type.


'''


class Solution:
    def isValid(self, s: str) -> bool:
        # setUp a map of closing and starting brackets, 
        # since it is given there will be only brackets in the input string
        Map = {')': '(', '}': '{', ']': '['} # Since, when matched closing is found we remove from the top we make closing ones the key for the map
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
        return not stack
    

        