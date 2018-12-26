class GraphNode {
    protected char: string;
    protected adjacents;
    constructor(char: string) {
        this.char = char;
        this.adjacents = new Map<string, Node>();
    }

}

class Graph {
    protected nodes = new Map();
    add(char: string) {
        if (this.nodes.has(char) === false) {
            this.nodes.set(char, new GraphNode(char));
        }
    }

    addWord(w: string) {
        const words = w.split('');
        let startNode = this.nodes.get(words[0]);
        if (startNode) {
            for (let i = 1; i < words.length; i++) {
                if (startNode.has(words[i])) {
                    startNode = startNode.get(words[i]);
                } else {
                    let newNode = new GraphNode(words[i]);
                    startNode.set(words[i], newNode);
                    startNode = newNode;
                }
            }
        }

    }
}


function findWord(graph, w) {
    //split words into characters
    const words = w.split('');

    // iterate over each char
    let node = graph.get(words[0]);
    if (!node) {
        return false;
    }

    for (let i = 1; i < words.length; i++) {
        // find the node for the given char
        const char = words[i];
        // if not found, return false
        if (node.has(char) === false) {
            return false;
        }

        // if found, return a node
        node = node.get(char);
    }
    // return true when loop ends
    return true;
}
