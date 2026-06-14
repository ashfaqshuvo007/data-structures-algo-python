
#* 261. Graph Valid Tree - MEDIUM

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

#? Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true

#? Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false

#? Note:

You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] 
and thus will not appear together in edges.

"""


from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        # Create adjacency List
        adjList = [[] for _ in range(n)]
        for p, c in edges:
            adjList[p].append(c)
            adjList[c].append(p)

        visited = set()
        def dfs(node, parent):
            if node in visited: #Cycle Detected
                return False

            visited.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                # running dfs on all neighbors
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n
