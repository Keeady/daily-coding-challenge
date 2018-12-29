from Graph import Graph


def test_all_path():
    graph = Graph.Graph()
    graph.add_path('June', 'Mary', 'cast away')
    path = graph.print_graph(None)
    assert path == ['June', 'Mary']


def test_from_one_path():
    graph = Graph.Graph()
    graph.add_path('June', 'Mary', 'cast away')
    path = graph.print_graph('Mary')
    assert path == ['Mary', 'June']
    path = graph.print_graph('June')
    assert path == ['June', 'Mary']


def test_from_two_path():
    graph = Graph.Graph()
    graph.add_path('June', 'Mary', 'cast away')
    graph.add_path('June', 'Kevin', 'cast away')
    path = graph.print_graph('Mary')
    assert path == ['Mary', 'June', 'Kevin']
    path = graph.print_graph('Kevin')
    assert path == ['Kevin', 'June', 'Mary']


def test_from_distinct_path():
    graph = Graph.Graph()
    graph.add_path('June', 'Mary', 'cast away')
    assert len(graph.nodes) == 2
    graph.add_path('Julia', 'Kevin', 'pretty woman')
    assert len(graph.nodes) == 4
    path = graph.print_graph('Mary')
    assert path == ['Mary', 'June']
    path = graph.print_graph('Kevin')
    assert path == ['Kevin', 'Julia']


def test_multi_path():
    graph = Graph.Graph()
    graph.add_path('June', 'Mary', 'cast away')
    graph.add_path('June', 'Kevin', 'cast away')
    graph.add_path('Mary', 'Kevin', 'cast away')
    graph.add_path('Kevin', 'Jake', 'Love')
    graph.add_path('Jake', 'Amber', 'pretty woman')
    graph.add_path('Jake', 'Mannie', 'pretty woman')
    graph.add_path('Mannie', 'Amber', 'pretty woman')

    assert len(graph.nodes) == 6
    path = graph.print_graph('Mary')
    assert path == ["Mary", "June", "Kevin", "Jake", "Amber", "Mannie"]
    path = graph.print_graph('June')
    assert path == ["June", "Mary", "Kevin", "Jake", "Amber", "Mannie"]
    path = graph.print_graph('Amber')
    assert path == ["Amber", "Jake", "Mannie", "Kevin", "June", "Mary"]
    path = graph.print_graph('Jake')
    assert path == ["Jake", "Kevin", "Amber", "Mannie", "June", "Mary"]