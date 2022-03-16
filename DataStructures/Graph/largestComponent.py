
def largestComponent(graph):
    # visited nodes list
    visited = []
    longestComponent = 0
    componentSize = 0

    #start traversal
    for node in graph:
        componentSize = int(explore(graph,node,visited))
        if componentSize > longestComponent: longestComponent = componentSize
    
    return longestComponent

#graph traversal helper
def explore(graph,current,visited):
    if (current in visited): return 0

    size = 1

    visited.append(current)
    for neighbour in graph[current]:
        size += explore(graph,neighbour,visited)

    #when all nodes of a component is visited
    return size



if __name__ == '__main__':
    graph = {
        0: [8,1,5],
        1: [0],
        5: [0,8],
        8: [0,5],
        2: [3,4],
        3: [2,4],
        4: [2,3]
    }

    print("Size of the largest Component: ",largestComponent(graph))