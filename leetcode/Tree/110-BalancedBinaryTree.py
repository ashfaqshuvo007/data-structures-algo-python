
#* Problem Statement

#* Given a binary tree, determin if it is height-balanced.

#? A height-balanced binary tree is a binary tree in which 
#? the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0] #balanced, height
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            balanced = leftHeight[0] and rightHeight[0] and abs(leftHeight[1] - rightHeight[1]) <= 1

            return [balanced, (1 + max(leftHeight[1], rightHeight[1]))]
        
        return dfs(root)[0]
    

if __name__ == "__main__":
    solution  = Solution()
#* Balanced Tree 
#   Input: root = [3,9,20,null,null,15,7]
    #Create a binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print("The Binary Tree is height-balanced: ", solution.isBalanced(root))

    #Create another skewed binary tree root = [1,2,2,3,3,null,null,4,4]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(3)
    root1.left.right.left = TreeNode(4)
    root1.left.right.right = TreeNode(4)
    print("The Binary Tree is height-balanced: ", solution.isBalanced(root1))

    root2 = []
    print("The Binary Tree is height-balanced: ", solution.isBalanced(root2))