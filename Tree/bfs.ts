function bfs(rootNode) {
    if (!rootNode) {
        return [];
    }

    let queue = [];
    let list = [];
    queue.push(rootNode);

    while (queue.length > 0) {
        let node = queue.shift();
        list.push(node.value);
        for (let index = 0; index < node.children.length; index++) {
            queue.push(node.children[index]);
        }
    }

    return list;
}

module.exports = bfs;
