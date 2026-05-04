
#* Problem Statement
#* Given the root of a binary tree, return its maximum depth.

#* A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#* Input: root = [3,9,20,null,null,15,7]
#* Output: 3


# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Easiest solution - recursive DFS - O(n)/O(n)
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



        # Iterative DFS - Using a stack storing node value and depth
        # stack = [[root, 1]] # node, depth
        # res = 0 # Handled in loop

        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
        # return res


        #======== Approach 3: BFS = Level Order Traversal =======#
        if not root:
            return 0

        q = collections.deque([root])
        level = 0 # 0 since, this is handle in loop

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


if __name__ == "__main__":
    solution  = Solution()
#  Input: root = [3,9,20,null,null,15,7]
    #Create a binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    maxDepth = solution.maxDepth(root)

    print("Max depth of the Tree: ", maxDepth)

