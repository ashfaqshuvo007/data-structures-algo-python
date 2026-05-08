
#* Problem statement

'''*
#* Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

#* Example 1
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

#* Example 2
Input: root = [1]
Output: [[1]]

#* Example 3
Input: root = []
Output: []
'''

# Definition for a binary tree node.

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # ======== Aproach 1 - Iterative BFS ========    

        # if not root:
        #     return []
        # q = collections.deque([root])
        # result = []

        # while q:
        #     levelArr = []
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         levelArr.append(node.val)

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     result.append(levelArr)
        # return result
        

        # ======== Aproach 2 - Recursive DFS ========  
        res = [] # [[]]

        def dfs(node, d):
            if not node:
                return None
            
            if len(res) == d:
                res.append([])
            
            res[d].append(node.val)
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
        
        dfs(root, 0)
        return res