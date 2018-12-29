from Graph import MovieGraph

def test_no_path():
    movies = {
        "cast away": ["June", "Mary", "Kevin"],
        "pretty woman": ["Jake", "Julia"],
        "lie to me": ["Amber", "Mannie"]
    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    assert len(movie_graph.print_all_path(graph)) == 7
    path = movie_graph.print_path(graph, "June")
    assert path == ["June", "Mary", "Kevin"]


def test_same_path():
    movies = {
        "cast away": ["June", "Mary", "Kevin"],
        "pretty woman": ["Jake", "Julia"],
        "lie to me": ["Amber", "Mannie"]
    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    paths = movie_graph.print_shortest_path(graph, "Julia", "Julia")
    assert paths == ["Julia"]
    bacon_number = movie_graph.print_bacon_number(graph, "Julia", "Julia")
    assert bacon_number == 0

def test_no_hop_path():
    movies = {
        "cast away": ["June", "Mary", "Kevin"],
        "pretty woman": ["Jake", "Julia"],
        "lie to me": ["Amber", "Mannie"]
    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    paths = movie_graph.print_shortest_path(graph, "Julia", "Kevin")
    assert paths == []
    bacon_number = movie_graph.print_bacon_number(graph, "Julia", "Kevin")
    assert bacon_number == -1


def test_zero_hop_path():
    movies = {
        "cast away": ["June", "Mary", "Kevin"],
        "pretty woman": ["Jake", "Julia"],
        "lie to me": ["Amber", "Mannie"]
    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    paths = movie_graph.print_shortest_path(graph, "June", "Kevin")
    assert paths == ["June", "Kevin"]
    bacon_number = movie_graph.print_bacon_number(graph, "June", "Kevin")
    assert bacon_number == 1


def test_one_hop_path():
    movies = {
        "cast away": ["June", "Mary", "Kevin"],
        "pretty woman": ["Jake", "Marc", "Kevin"],
        "lie to me": ["Amber", "Mannie", "Jake"]
    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    paths = movie_graph.print_shortest_path(graph, "June", "Jake")
    assert paths == ["June", "Kevin", "Jake"]
    bacon_number = movie_graph.print_bacon_number(graph, "June", "Jake")
    assert bacon_number == 2


def test_two_hop_path():
    movies = {
        "cast away": ["June", "Mary", "Kevin"],
        "pretty woman": ["Jake", "Kevin"],
        "lie to me": ["Amber", "Jake"],
        "lie to me 2": ["Claudette", "Amber"],
        "lie": ["Claudette", "Patrick"],
        "love": ["Brian", "Patrick"],
        "self love": ["Krauss", "Patrick"]
    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    paths = movie_graph.print_shortest_path(graph, "June", "Krauss")
    assert paths == ["June", "Kevin", "Jake", "Amber", "Claudette", "Patrick", "Krauss"]
    bacon_number = movie_graph.print_bacon_number(graph, "June", "Krauss")
    assert bacon_number == 6

def test_multi_hop_path():
    movies = {
        "cast away": ["June", "Mary", "Kevin"],
        "pretty woman": ["Jake", "Xor", "Kevin"],
        "lie to me": ["Amber", "Paul", "Jake"],
        "lie to me 2": ["Claudette", "Amber"],
        "lie": ["Claudette", "Patrick"],
        "love": ["Brian", "Kris"],
        "Food": ["Brian", "Kris"],
        "self love": ["Krauss", "Patrick"]
    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    paths = movie_graph.print_shortest_path(graph, "June", "Krauss")
    assert paths == ["June", "Kevin", "Jake", "Amber", "Claudette", "Patrick", "Krauss"]
    bacon_number = movie_graph.print_bacon_number(graph, "June", "Krauss")
    assert bacon_number == 6

def test_multi_nohop_path():
    movies = {
        "cast away": ["June", "Mary", "Kevin"],
        "pretty woman": ["Jake", "Xor", "Kevin"],
        "lie to me": ["Amber", "Paul", "Jake"],
        "lie to me 2": ["Claudette", "Amber"],
        "lie": ["Claudette", "Patrick"],
        "love": ["Brian", "Kris"],
        "Food": ["Brian", "Kris"],
        "self love": ["Krauss", "Karl"]
    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    paths = movie_graph.print_shortest_path(graph, "June", "Krauss")
    assert paths == []
    bacon_number = movie_graph.print_bacon_number(graph, "June", "Krauss")
    assert bacon_number == -1

def test_multi_short_hop_path():
    movies = {
        "cast away": ["June", "Mary", "Kevin"],
        "pretty woman": ["Jake", "Xor", "Kevin"],
        "lie to me": ["Amber", "Paul", "Jake"],
        "lie to me 2": ["Claudette", "Amber"],
        "lie": ["Claudette", "Patrick"],
        "love": ["Brian", "Kris"],
        "Food": ["Brian", "Kris"],
        "self love": ["Krauss", "Karl"],
        "dance": ["Krauss", "Paul"]

    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    paths = movie_graph.print_shortest_path(graph, "June", "Krauss")
    assert paths == ["June", "Kevin", "Jake", "Paul", "Krauss"]
    bacon_number = movie_graph.print_bacon_number(graph, "June", "Krauss")
    assert bacon_number == 4

def test_multi_short_hop_path2():
    movies = {
        "cast away": ["June", "Mary", "Kevin", "Paul"],
        "pretty woman": ["Jake", "Xor", "Kevin"],
        "lie to me": ["Amber", "Xavier", "Jake"],
        "lie to me 2": ["Claudette", "Amber"],
        "lie": ["Claudette", "Patrick"],
        "love": ["Brian", "Kris"],
        "Food": ["Brian", "Kris"],
        "self love": ["Krauss", "Karl"],
        "dance": ["Krauss", "Paul"]
    }
    movie_graph = MovieGraph.MovieGraph(movies)
    graph = movie_graph.build_movie_graph()
    paths = movie_graph.print_shortest_path(graph, "June", "Krauss")
    assert paths == ["June", "Paul", "Krauss"]
    bacon_number = movie_graph.print_bacon_number(graph, "June", "Krauss")
    assert bacon_number == 2
