function findMaxConnectComponent(componentMatrix) {
    var max = 0;
    var row, col = 0;
    var count;
    for (row = 0; row < componentMatrix.length; row++) {
        for (col = 0; col < componentMatrix[0].length; col++) {
            if (componentMatrix[row][col] === 1) {
                count = visit(componentMatrix, row, col);
                if (count > max) {
                    max = count;
                }
            }
        }
    }
    return max;
}
function isValid(row, col, componentMatrix) {
    return row >= 0 && row < componentMatrix.length && col >= 0 && col < componentMatrix.length &&
        componentMatrix[row][col] === 1;
}
function visit(componentMatrix, row, col) {
    var count = 0;
    var queue = [];
    var currentPos;
    queue.push([row, col]);
    while (queue.length > 0) {
        currentPos = queue.shift();
        row = currentPos[0];
        col = currentPos[1];
        componentMatrix[row][col] = -1;
        count += 1;
        if (isValid(row - 1, col, componentMatrix)) {
            queue.push([row - 1, col]);
        }
        if (isValid(row + 1, col, componentMatrix)) {
            queue.push([row + 1, col]);
        }
        if (isValid(row, col - 1, componentMatrix)) {
            queue.push([row, col - 1]);
        }
        if (isValid(row, col + 1, componentMatrix)) {
            queue.push([row, col + 1]);
        }
    }
    return count;
}
module.exports = findMaxConnectComponent;
//[
// [0, -1, -1, 0],
// [0, -1,  0,  -1],
// [1,  0,   -1,  -1],
// [0, 0, 0, 0],
// [1, 0, 0,     1]]
//max=3
//r=1 c=3
//q=[] count=3
//pos=2,2
