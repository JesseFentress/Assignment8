import sys

class WeightedGraph:

    def __init__(self, graph_dict):
        if graph_dict is None:
            graph_dict

        self.graph_dict = graph_dict

    def get_keys(self):
        keys = []  # List to hold keys
        for vertex in self.graph_dict:  # Iterate through all the keys
            keys.append(vertex)  # Add key to keys
        return keys  # Return list of keys

    def dijkstra(self, start_index):
        unvisited = self.get_keys()
        print(unvisited)
        path = {}
        vertices = {}
        maximum = sys.maxsize
        for vertex in unvisited:
            path[vertex] = maximum

        path[start_index] = 0
        print(path)

        while unvisited:
            min_vertex = None
            for vertex in unvisited:
                if min_vertex is None:
                    min_vertex = vertex
                elif path[vertex] < path[min_vertex]:
                    min_vertex = vertex
            edges = list(self.graph_dict[min_vertex[:]])

            for edge in edges:
                temp = path[min_vertex] + 23


places = {
    'A': set([('B', 10), ('C', 5)]),
    'B': set([('D', 3), ('A', 10)]),
    'C': set([('F', 20), ('G', 9), ('A', 5)]),
    'D': set([('B', 3)]),
    'F': set([('C', 20)]),
    'G': set([('C', 9)])
}

wg = WeightedGraph(places)
wg.dijkstra('B')