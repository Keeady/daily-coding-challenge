function dfs(rootNode, list = []) {
    if (!rootNode) {
        return list;
    }

    list.push(rootNode.value);
    if (rootNode.children.length === 0) {
        return list;
    }

    for (let index = 0; index < rootNode.children.length; index++) {
        dfs(rootNode.children[index], list);
    }

    return list;
}

module.exports = dfs;
