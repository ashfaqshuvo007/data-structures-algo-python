
#* 572 - Subtree of Another Tree

#? Test cases:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self._sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) 
    
    def _sameTree(self, r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return (self._sameTree(r.left, s.left)) and (self._sameTree(r.right, s.right))
        return False
        