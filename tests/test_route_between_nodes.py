from Graph import route_between_nodes
from Graph import Graph


def test_find_route():
    graph = Graph.Graph()
    graph.add_direct_path('June', 'Mary', 'cast away')
    graph.add_direct_path('June', 'Kevin', 'cast away')
    graph.add_direct_path('Mary', 'Kevin', 'cast away')
    graph.add_direct_path('Kevin', 'Jake', 'Love')
    graph.add_direct_path('Jake', 'Amber', 'pretty woman')
    graph.add_direct_path('Jake', 'Mannie', 'pretty woman')
    graph.add_direct_path('Mannie', 'Amber', 'pretty woman')
    graph.add_direct_path('Amber', 'Mary', 'pretty woman')

    assert True == route_between_nodes.route_between_nodes(graph, 'Mary', 'Kevin')

    assert True == route_between_nodes.route_between_nodes(graph, 'June', 'Jake')

    assert False == route_between_nodes.route_between_nodes(graph, 'Mannie', 'June')

    assert True == route_between_nodes.route_between_nodes(graph, 'Mannie', 'Kevin')

    assert True == route_between_nodes.route_between_nodes(graph, 'Mannie', 'Jake')

    assert True == route_between_nodes.route_between_nodes(graph, 'Mannie', 'Mannie')