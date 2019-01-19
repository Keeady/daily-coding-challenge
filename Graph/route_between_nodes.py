from Graph import GraphNode
import queue

def route_between_nodes(graph, nodeKeyA, nodeKeyB):
    nodeA = graph.get_node(nodeKeyA)
    nodeB = graph.get_node(nodeKeyB)

    if not nodeA or not nodeB:
        return False

    if nodeA == nodeB:
        return True

    if nodeA.has_path(nodeB) or nodeB.has_path(nodeA):
        return True

    return visit_graph(nodeA, nodeB)


def visit_graph(start: GraphNode, dest: GraphNode):
    visit_queue = queue.Queue()
    # add first node into visit queue
    visit_queue.put(start)
    visited_map = {}

    while not visit_queue.empty():
        node = visit_queue.get()
        visited_map[node] = True

        if node.has_path(dest) or node == dest:
            return True

        for edge_name in node.edges:
            edge = node.edges[edge_name]
            if edge.destination not in visited_map:
                visit_queue.put(edge.destination)

    return False