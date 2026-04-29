# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Reverse 
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)


        return root
    

    # function to print the tree in level order traversal
    def print_tree(root):
        if not root:
            return None
        
        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.val, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        



if __name__ == "__main__":
    solution  = Solution()

    #Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    inverte_tree = solution.invertTree(root)

    #print the tree in level order traversal
