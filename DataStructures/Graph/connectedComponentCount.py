
def connectedComponentCount(graph):
    # visited nodes list
    visited = []
    count = 0

    #start traversal
    for node in graph:
        if(explore(graph,node,visited)) == True:
            count += 1
    

    return count

#graph traversal helper
def explore(graph,current,visited):
    if (current in visited): return False

    visited.append(current)

    for neighbour in graph[current]:
        explore(graph,neighbour,visited)

    #when all nodes of a component is visited
    return True



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

    print("Number of connected components: ",connectedComponentCount(graph))