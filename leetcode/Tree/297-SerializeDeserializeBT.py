
#* Problem Statement
#* 297. Serialize and Deserialize Binary Tree - HARD
'''
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection 
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string c
an be deserialized to the original tree structure.

Examples:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Input: root = []
Output: []

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    #* DFS - Preorder Traversal - O(n)/O(n)
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        values = data.split(",")
        self.index = 0

        def dfs():
             # base case
            if values[self.index] == "N":
                self.index += 1
                return None
            
            root = TreeNode(int(values[self.index]))
            self.index += 1

            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))