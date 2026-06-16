
#* 323. Number of Connectred Components in an Undirected Graph - MEDIUM

'''
You have a graph of n nodes. You are given an integer n and an array edges 
where edges[i] = [aᵢ, bᵢ] indicates that there is an edge 
between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.

#? Exmaple 1:
Input:
n = 5, edges = [[0,1],[1,2],[3,4]]

Output: 2

#? Example 2:
Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]

Output: 1
'''
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency List
        adjList = [[] for _ in range(n)]
        for p, c in edges:
            adjList[p].append(c)
            adjList[c].append(p)
        
        visit = [False] * n
        def dfs(node):
            for nei in adjList[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res
