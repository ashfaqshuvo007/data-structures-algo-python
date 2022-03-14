
# Get the undirected path between nodes

def undirectedGraphPath(edges,nodeA,nodeB):
    # Make the adjacency list form the given adjacency list
    graph = buildGraph(edges)
    
    # Check if path exists between two nodes
    return hasPath(graph,nodeA,nodeB,visited = [])

#has path helper

def hasPath(graph,src,dest,visited):
    if(src == dest): return True

    # Make sure to check for cycles as
    # the given graph edge list is undirected
    if src in visited: return False
    visited.append(src)

    for neighbour in graph[src]:
       if hasPath(graph,neighbour,dest,visited): return True
    
    return False



# Adjacency list helper
def buildGraph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph



if __name__ == '__main__':
    edges = [
        ['i','j'],
        ['k','i'],
        ['m','k'],
        ['k','l'],
        ['o','n'],
    ]

    print(undirectedGraphPath(edges,'i','k'))
