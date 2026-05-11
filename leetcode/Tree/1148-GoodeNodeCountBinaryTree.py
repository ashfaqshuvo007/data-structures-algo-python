import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ## ===== Approach 1 ======== ##
        # DFS - Initializing with root.val as the max. 
        # Always update max with max(current Node value, current Max value)

        # def dfs(node, maxi):
        #     if not node:
        #         return 0
            
        #     if node.val >= maxi:
        #         res = 1
        #     else:
        #         res = 0

        #     res += dfs(node.left, max(maxi, node.val))
        #     res += dfs(node.right, max(maxi, node.val))

        #     return res
        # return dfs(root, root.val)

        ## ===== Approach 2 ======== ##
        # DFS - With global count of Good Nodes 
        # Always update max with max(current Node value, current Max value)
        # Update count each recursive call

        # count = 0

        # def dfs(node, maxi = -float("inf")):
        #     if not node:
        #         return 
        #     nonlocal count
        #     if node.val >= maxi:
        #         count += 1
        #         maxi = node.val
            
        #     dfs(node.left, maxi)
        #     dfs(node.right, maxi)
        
        # dfs(root)

        # return count

        ## ===== Approach 3 ======== ##
        # BFS - Using queue - with tuple(node, - float("inf"))
        # Always update max with max(current Node value, current Max value), give in each recursive call
        # Update count each recursive call
       
        res = 0
        q = collections.deque()

        q.append((root, -float("inf")))

        while q:
            node,maxi = q.popleft()
        
            if node.val >= maxi:
                res += 1
            
            # Recursion with current maxValue
            if node.left:
                q.append((node.left, max(node.val, maxi)))
            if node.right:
                q.append((node.right, max(node.val, maxi)))
        
        return res
