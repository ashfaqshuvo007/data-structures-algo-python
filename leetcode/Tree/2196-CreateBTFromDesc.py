
#* 2196. Create Binary Tree From Descriptions - MEDIUM - Leetcode Daily Contest

'''

You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that 
parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

#? Example 2:

Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

#? Example 2:

Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
'''


from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        #* Approach 1: Iteration with Hashing
        #* Time: O(n) Space: O(n)
        nodes = {} # All nodes for reference
        children = set() # All child nodes, later used to find root.

        for parent, child, is_left in descriptions:
            # Add all node to children, helps in find root as it won't be in child pos
            children.add(child)
            # Create Nodes with all values
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            # Arrange the nodes in left or right
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for p, c, l in descriptions:
            if p not in children:
                return nodes[p]