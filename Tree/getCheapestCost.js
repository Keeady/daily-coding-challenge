function getCheapestCost(rootNode) {
    return calcCost(Number.MAX_VALUE, 0, rootNode);
}
function calcCost(minCost, parentCost, node) {
    if (node === null) {
        return 0;
    }
    if (node.children.length === 0) {
        return Math.min(minCost, parentCost + node.cost);
    }
    parentCost += node.cost;
    for (var i = 0; i < node.children.length; i++) {
        minCost = calcCost(minCost, parentCost, node.children[i]);
    }
    return minCost;
}
module.exports = getCheapestCost;
