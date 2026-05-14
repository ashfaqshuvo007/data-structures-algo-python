
#* Problem Statement:

#* 230. Kth Smallest Element in a BST - Medium
#* Given the root of a binary search tree, and an integer k, 
#* return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

#? Examples:

'''
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''


from collections import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # AProach 1 - DFS with In-order traversal
        # nodesArr = [] # Keep track of visited nodes. Yields a sorted array. Take the kth element from it
        # def dfs(node):
        #     if not node:
        #         return

        #     dfs(node.left)
        #     nodesArr.append(node.val)
        #     dfs(node.right)
        
        # dfs(root)
        # return nodesArr[k - 1] # 1 - indexed (so k -1 is the result not K)


        #Aproach 2: Optimal DFS with IN-Order Traversal
        # WHile traversing, keeping count and if count == 0 , we found the solution
        # WE visit left-subtree only when Kth element is not found.

        cnt = k
        res = 0

        def dfs(node):
            if not node:
                return
            
            nonlocal cnt, res
            dfs(node.left)

            if cnt == 0:
                return # Result already found
            
            #decrement
            cnt -= 1

            if cnt == 0:
                res = node.val # Result found
                return
            # IF result not found yet, visit right subtree
            dfs(node.right)
            
        dfs(root)
        return res
        