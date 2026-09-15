class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                paths = list.copy(new_paths)

        return paths

    def get_shortest_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp and (shortest_path is None or len(sp) < len(shortest_path)):
                    shortest_path = sp

        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "New York"),
        ("Paris", "Dubai"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    route_graph = Graph(routes)

    start = "Mumbai"
    end = "Dubai"
    print(f"Paths between {start} and {end}: {route_graph.get_paths(start, end)}")
    print(
        f"The shortest path between Paris and New York is {route_graph.get_shortest_path('Paris', 'Toronto')}"
    )
