
#* Problem Statement: 

#* Leetcode 98. Validate Binary Search Tree - Medium

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

 - The left subtree of a node contains only nodes with keys strictly less than the node's key.
 - The right subtree of a node contains only nodes with keys strictly greater than the node's key.
 - Both the left and right subtrees must also be binary search trees.

'''
#? Examples:

'''
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false

Input: root = [0]
Output: True

'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #? Recursive DFS - O(n) time and space
        #? My mistake was that I left out the root of the TREE while recursively checking the subtrees.

        #? Awesome Idea from NEETCODE -  having max and min bounds for recursion.
        def valid(node, minBound, maxBound):
            if not node:
                return True
            if not (minBound < node.val < maxBound):
                return False
            
            #? THis is where the magic happens. while in left subtree max is currNode's val
            #? And while in right subtree min is currNode's val
            return (valid(node.left, minBound, node.val) and
                    valid(node.right, node.val, maxBound))

        return valid(root, float("-inf"), float("inf"))
        