from Graph import GraphNode
from Graph import GraphEdge


def test_add():
    mary = GraphNode.GraphNode('Mary')
    june = GraphNode.GraphNode('June')
    mary.add_path(june, 'cast away')

    assert len(mary.edges) == 1
    assert len(june.edges) == 0

    june.add_path(mary, 'cast away')
    assert len(june.edges) == 1

    kevin = GraphNode.GraphNode('Kevin')
    june.add_path(kevin, 'cast away')

    assert len(june.edges) == 2
    assert len(kevin.edges) == 0

    kevin.add_path(june, 'cast away')
    assert len(kevin.edges) == 1

    amber = GraphNode.GraphNode('Amber')
    kevin.add_path(amber, 'pretty woman')
    amber.add_path(kevin, 'pretty woman')

    assert len(june.edges) == 2
    assert len(kevin.edges) == 2
    assert len(mary.edges) == 1
    assert len(amber.edges) == 1

    mary.add_path(kevin, 'cast away')
    kevin.add_path(mary, 'cast away')
    assert len(mary.edges) == 2
    assert len(kevin.edges) == 3
