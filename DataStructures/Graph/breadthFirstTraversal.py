
# Using Iterative method
def breadthFirstTraversal(graph, source):
    visited = []
    queue = []
    queue.append(source)
    visited.append(source)

    while (len(queue) > 0):
        current = queue.pop(0)
        print(current,end=" ")

        for neighbour in graph[source]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
               


if __name__ == "__main__":
    graph = {
        "a": ['b', 'c'],
        "b": ['d'],
        "c": ['e'],
        "d": ['f'],
        "e": [],
        "f": [],
    }
    breadthFirstTraversal(graph, 'a')
