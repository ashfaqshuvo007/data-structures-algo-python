# Graph is recursive data structure a bit like tree.
# You can think of graph  as a special type of tree.
# But Graphs can have multiple random paths connecting two nodes.
# Unlike trees which only have one path between two nodes.

# Code snippet below is a python implementation of Graph.
# Implements two methods: shortest path & all possible path

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for s, e in self.edges:
            if s in self.graph_dict:
                self.graph_dict[s].append(e)
            else:
                self.graph_dict[s] = [e]

        print("Graph Dictionary: ", self.graph_dict)

    def get_paths(self, starting_point, destination, path=[]):
        path = path + [starting_point]
        # when there is one node
        if starting_point == destination:
            return [path]
        # when node is not in our graph
        if starting_point not in self.graph_dict:
            return []

        all_paths = []

        for node in self.graph_dict[starting_point]:
            if node not in path:
                new_paths = self.get_paths(node, destination, path)
                for p in new_paths:
                    all_paths.append(p)

        return all_paths

    def get_shortest_path(self, starting_point, destination, path=[]):
        path = path + [starting_point]

        if starting_point == destination:
            return path

        if starting_point not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[starting_point]:
            if node not in path:
                sp = self.get_shortest_path(node, destination, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    start = "Paris"
    end = "New York"

    # print(f"Paths from {start} to {end}: ", route_graph.get_paths(start, end))

    print(f"Shortest Path from {start} to {end}: ", route_graph.get_shortest_path(start, end))
