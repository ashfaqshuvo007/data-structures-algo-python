
#** Problem Statement

'''
#* Given the root of a binary tree, return the length of the diameter of the tree.

#* The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#* The length of a path between two nodes is represented by the number of edges between them.

'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #? Recursive DFS
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def dfs(node):
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            self.d = max(self.d, (leftHeight + rightHeight))

            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)

        return self.d
    
if __name__ == "__main__":
    solution  = Solution()
    #* Balanced Tree 
    #   Input: root = [1,2,3,4,5]
    #Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    diameter = solution.diameterOfBinaryTree(root)

    print("Diameter of a Binary tree [1, 2, 3, 4, 5]: ", diameter)

    #   Input: root = [1,2]
    #Create a binary tree
    tree = TreeNode(1)
    tree.left = TreeNode(2)

    diameter1 = solution.diameterOfBinaryTree(tree)

    print("Diameter of a Binary tree [1, 2]: ", diameter1)