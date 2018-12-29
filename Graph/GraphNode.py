from Graph import GraphEdge

class GraphNode:
    def __init__(self, name):
        self.name = name
        self.edges = {}

    def add_path(self, node, edge_name):
        if node.name not in self.edges:
            edge = GraphEdge.GraphEdge(edge_name, node)
            self.edges[node.name] = edge

