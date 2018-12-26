var GraphNode = /** @class */ (function () {
    function GraphNode(char) {
        this.char = char;
        this.adjacents = new Map();
    }
    return GraphNode;
}());
var Graph = /** @class */ (function () {
    function Graph() {
        this.nodes = new Map();
    }
    Graph.prototype.add = function (char) {
        if (this.nodes.has(char) === false) {
            this.nodes.set(char, new GraphNode(char));
        }
    };
    Graph.prototype.addWord = function (w) {
        var words = w.split('');
        var startNode = this.nodes.get(words[0]);
        if (startNode) {
            for (var i = 1; i < words.length; i++) {
                if (startNode.has(words[i])) {
                    startNode = startNode.get(words[i]);
                }
                else {
                    var newNode = new GraphNode(words[i]);
                    startNode.set(words[i], newNode);
                    startNode = newNode;
                }
            }
        }
    };
    return Graph;
}());
function findWord(graph, w) {
    //split words into characters
    var words = w.split('');
    // iterate over each char
    var node = graph.get(words[0]);
    if (!node) {
        return false;
    }
    for (var i = 1; i < words.length; i++) {
        // find the node for the given char
        var char = words[i];
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
