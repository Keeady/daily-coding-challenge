from Graph import Graph


class MovieGraph:
    def __init__(self, movies):
        self.movies = movies
        self.graph = Graph.Graph()

    def build_movie_graph(self):
        for name in self.movies:
            actors = self.movies[name]
            for actor1 in actors:
                for actor2 in actors:
                    if actor1 != actor2:
                        self.graph.add_path(actor1, actor2, name)
        return self.graph

    def print_path(self, graph, actor):
        return graph.print_graph(actor)

    def print_all_path(self, graph):
        return graph.print_graph(None)

    def print_shortest_path(self, graph, actor1, actor2):
        return graph.find_path(actor1, actor2)

    def print_bacon_number(self, graph, actor1, actor2):
        return graph.find_bacon_number(actor1, actor2)