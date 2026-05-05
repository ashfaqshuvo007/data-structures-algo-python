
# * 
# * P.S.
# *The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# */

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1 + self.minDepth(root.left or root.right) 
        


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

    minDepth = solution.minDepth(root)

    print("Min depth of the Tree: ", minDepth)
#* More skewed Tree

    #Create another skewed binary tree [2,null,3,null,4,null,5,null,6]
    root1 = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.right = TreeNode(4)
    root1.right.right.right = TreeNode(5)
    root1.right.right.right.right = TreeNode(6)

    minDepth1 = solution.minDepth(root1)

    print("Min depth of the Tree: ", minDepth1)