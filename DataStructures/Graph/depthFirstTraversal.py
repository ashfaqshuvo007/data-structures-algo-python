
# Using Iterative method
def depthFirstTraversalIterative(graph,source):
    stackData = []
    stackData.append(source)
    while(len(stackData) > 0):
        current = stackData.pop()
        print(current)

        for i in graph[current]:
            stackData.append(i)

#Using Recursion
def depthFirstTraversalRecursion(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthFirstTraversalRecursion(graph,neighbour)
    

if __name__ == "__main__":
    graph = {
        "a": ['c','b'],
        "b": ['d'],
        "c": ['e'],
        "d": ['f'],
        "e": [],
        "f": [],
    }
    # depthFirstTraversalIterative(graph, 'a')
    depthFirstTraversalRecursion(graph, 'a')
