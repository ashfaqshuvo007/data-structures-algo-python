
#* Problem Statement: Leetcode - 199 MEDIUM

#* Given the root of a binary tree, imagine yourself standing on the right side of it, 
#*  return the values of the nodes you can see ordered from top to bottom.

#* Examples:

#? Example1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

#? Example2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]

#? Example 3:
# Input: root = [1,null,3]
# Output: [1,3]

#? Example 4:
# Input: root = []
# Output: []

import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #? APROACH 1: Interative BFS - O(n)/ O(n + m)
        if not root:
            return []
        
        q = collections.deque([root])
        res = []

        while q:
            levelArr = []
            for _ in range(len(q)):
                cur = q.popleft()

                levelArr.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
            res.append(levelArr[-1])
        return res

        # APROACH 2: Recursive DFS 
        #? Complexity - O(n) / O(n)
        # res = []

        # def dfs(node, depth):
        #     if not node:
        #         return None
            
        #     if depth == len(res):
        #         res.append(node.val)
            
        #     dfs(node.right, depth + 1) # Always right subtree first
        #     dfs(node.left, depth + 1)
        
        # dfs(root, 0)

        # return res