def shortestPath(edges,src,dest):
    # build adjacency list
    graph = buildGraph(edges)
    # {'w': ['x', 'v'], 'x': ['w', 'y'], 'y': ['x', 'z'],
    #  'z': ['y', 'v'], 'v': ['z', 'w']}
    #visited list and queue with src and distance initialized
    visited = [src]
    queue = []
    queue.append([src,0])
    

    while len(queue) > 0:
        node,distance = queue.pop(0)

        if node == dest: return distance

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append((neighbour,distance + 1))

    # Return anything mentioned in the problem definition
    return visited



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
        ['w','x'],
        ['x','y'],
        ['z','y'],
        ['z','v'],
        ['w','v']
    ]

    print("The shortest path : ",shortestPath(edges,'w','z'))
    # print(shortestPath(edges))