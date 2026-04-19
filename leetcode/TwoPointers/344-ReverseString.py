# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


"""
Do not return anything, modify s in-place instead.
"""
# Two pointer pattern
s = ["h","e","l","l","o"]
l, r = 0, len(s) - 1

while l < r:
    s[l], s[r] = s[r], s[l]
    l, r = l + 1, r - 1