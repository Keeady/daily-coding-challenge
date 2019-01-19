from Graph import GraphNode, GraphEdge
import queue

class Graph:

    def __init__(self):
        self.nodes = {}

    def get_node(self, name):
        if name not in self.nodes:
            return None

        return self.nodes[name]

    def add_direct_path(self, actor1, actor2, movie):
        # path from actor1 to actor2

        if actor1 in self.nodes:
            node1 = self.nodes[actor1]
        else:
            node1 = GraphNode.GraphNode(actor1)

        if actor2 in self.nodes:
            node2 = self.nodes[actor2]
        else:
            node2 = GraphNode.GraphNode(actor2)

        node1.add_path(node2, movie)

        self.nodes[actor1] = node1
        self.nodes[actor2] = node2

    def add_path(self, actor1, actor2, movie):
        if actor1 in self.nodes:
            actor_node1 = self.nodes[actor1]
        else:
            actor_node1 = GraphNode.GraphNode(actor1)

        if actor2 in self.nodes:
            actor_node2 = self.nodes[actor2]
        else:
            actor_node2 = GraphNode.GraphNode(actor2)

        actor_node1.add_path(actor_node2, movie)
        actor_node2.add_path(actor_node1, movie)

        self.nodes[actor1] = actor_node1
        self.nodes[actor2] = actor_node2

    def print_graph(self, name):
        path = []
        nodeQueue = queue.Queue()
        visited = {}

        if name is None:
            for name in self.nodes:
                path.append(name)
            return path
        else:
            nodeQueue.put(self.nodes[name])

        while not nodeQueue.empty():
            node = nodeQueue.get()
            if node.name in visited:
                continue

            path.append(node.name)
            visited[node.name] = node
            for edge_name in node.edges:
                edge = node.edges[edge_name]
                if edge.destination.name not in visited:
                    nodeQueue.put(edge.destination)
        return path

    def find_path(self, actor1: GraphNode, actor2: GraphNode):
        path = []
        if actor1 not in self.nodes or actor2 not in self.nodes:
            return path

        if actor1 == actor2:
            return [actor1]

        source: GraphNode = self.nodes[actor1]
        dest: GraphNode = self.nodes[actor2]

        visited1 = {}
        visited2 = {}

        '''
        self.__traverse(source, dest, visited1, visited2)

        path1 = self.__print_path(source, visited2, dest)
        path2 = self.__print_path(dest, visited1, source)

        if len(path1) > 0:
            path1.insert(0, source.name)
            return path1
        elif len(path2) > 0:
            path2.insert(0, dest.name)
            path2.reverse()
            return path2

        '''
        visited_nodes = self.__traverse_single_direction(source, dest)
        path = self.__print_path(dest, visited_nodes, source)
        path.reverse()
        if len(path) > 0:
            path.append(dest.name)

        return path

    def find_bacon_number(self, actor1, actor2):
        if actor1 not in self.nodes or actor2 not in self.nodes:
            return -1

        if actor1 == actor2:
            return 0

        source: GraphNode = self.nodes[actor1]
        dest: GraphNode = self.nodes[actor2]

        return self.__traverse_bacon_nodes(source, dest)

    def __traverse_bacon_nodes(self, source, dest):
        pointer = source
        visited = {}
        visit_queue = queue.Queue()
        visit_queue.put(pointer)
        bacon_number = {pointer: 0}

        while not visit_queue.empty():
            pointer = visit_queue.get()
            visited[pointer] = bacon_number[pointer]

            if pointer == dest:
                return bacon_number[pointer]

            self.__visit_bacon_node(pointer, visit_queue, visited, bacon_number)

        return -1

    def __print_path(self, pointer, visited, end):
        path = []

        while pointer is not None and pointer != end:
            if pointer in visited and visited[pointer] is not None:
                pointer = visited[pointer]
                path.append(pointer.name)
            else:
                pointer = None

        return path

    def __traverse_single_direction(self, source, dest):
        pointer = source
        visited = {}
        visit_queue = queue.Queue()
        visit_queue.put(pointer)
        prev_nodes = {pointer: None}

        while not visit_queue.empty():
            pointer = visit_queue.get()

            visited[pointer] = prev_nodes[pointer]

            if pointer == dest:
                break

            tuple = self.__visit_node(pointer, visit_queue, visited, prev_nodes)
            visit_queue = tuple[0]
            prev_nodes = tuple[1]

        return visited

    def __traverse(self, source, dest, visited1, visited2):
        pointer1 = source
        pointer2 = dest

        queue1 = queue.Queue()
        queue1.put(pointer1)

        queue2 = queue.Queue()
        queue2.put(pointer2)

        prev_node1 = {pointer1: None}
        prev_node2 = {pointer2: None}

        while not queue1.empty() and not queue2.empty():
            pointer1 = queue1.get()
            pointer2 = queue2.get()

            visited1[pointer1] = prev_node1[pointer1]
            visited2[pointer2] = prev_node2[pointer2]

            tuple1 = self.__visit_node(pointer1, queue1, visited1, prev_node1)
            tuple2 = self.__visit_node(pointer2, queue2, visited2, prev_node2)

            queue1 = tuple1[0]
            prev_node1 = tuple1[1]

            queue2 = tuple2[0]
            prev_node2 = tuple2[1]

        return None

    def __visit_node(self, node, visit_queue, visited, previous_nodes):
        # gather neighbors of pointer2 into queue2
        for edge_name in node.edges:
            edge = node.edges[edge_name]
            if edge.destination not in visited:
                visit_queue.put(edge.destination)
            if edge.destination not in previous_nodes:
                previous_nodes[edge.destination] = node
        return (visit_queue, previous_nodes)

    def __visit_bacon_node(self, node, visit_queue, visited, bacon_number):
        # gather neighbors of pointer2 into queue2
        for edge_name in node.edges:
            edge = node.edges[edge_name]
            if edge.destination not in visited:
                visit_queue.put(edge.destination)
            if edge.destination not in bacon_number:
                bacon_number[edge.destination] = bacon_number[node] + 1
        return (visit_queue, bacon_number)
