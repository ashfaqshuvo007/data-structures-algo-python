# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #*  Recursive solution 1 - BEST on LEETCODE
        # if not root or root == p or root == q:
        #     return root

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        
        # if left and right:
        #     return root

        # return left or right
    
        #*  Recursive solution 2 - MINE works on NEETCODE
        # if root.val == p.val or root.val == q.val:
        #     return root

        # # Check if p and q both < root = traverse left subtree
        # if root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p , q)
        # # else traverse right subtree
        # elif root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root


        #* ITERATION - NEETCODE
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr