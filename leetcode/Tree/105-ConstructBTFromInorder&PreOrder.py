
#* Problem Statement
#* 105. Construct Binary Tree from Preorder and Inorder Traversal - MEDIUM
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and 
# inorder is the inorder traversal of the same tree, construct and return the binary tree.

'''
#? Constraints: 
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.


#? Examples:
#? Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#? Output: [3,9,20,null,null,15,7]


#? Input: preorder = [-1], inorder = [-1]
#? Output: [-1]
'''
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # Root is the 1st element in preorder
        root = TreeNode(preorder[0])

        #Finding root position to divide the tree
        pos = inorder.index(root.val)

        # Build the tree
        root.left = self.buildTree(preorder[1:pos+1], inorder[:pos])
        root.right = self.buildTree(preorder[pos+1:], inorder[pos + 1:])

        return root


