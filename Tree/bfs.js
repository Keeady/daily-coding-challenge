function bfs(rootNode) {
    if (!rootNode) {
        return [];
    }
    var queue = [];
    var list = [];
    queue.push(rootNode);
    while (queue.length > 0) {
        var node = queue.shift();
        list.push(node.value);
        for (var index = 0; index < node.children.length; index++) {
            queue.push(node.children[index]);
        }
    }
    return list;
}
module.exports = bfs;
