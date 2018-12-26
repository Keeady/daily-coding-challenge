function countIsland(binaryMatrix) {
    //iterate over each cell in matrix
    // if cell value == 1
        // increment count
        // add to queue
        // iterate over queue until empty
            // pop first ele
            // - mark as visited
            // gather neighbors that are == 1 and within matrix boundary
            // add them to a queue
    let rowIndex, colIndex, islandCount = 0, queue = [];
    for (rowIndex = 0; rowIndex < binaryMatrix.length; rowIndex++) {
        for (colIndex = 0; colIndex < binaryMatrix[0].length; colIndex++) {
            if (binaryMatrix[rowIndex][colIndex] === 1) {
                islandCount++;
                markVisited(binaryMatrix, rowIndex, colIndex);
            }
        }
    }

    return islandCount;
}

function markVisited(binaryMatrix, rowIndex, colIndex) {
    let queue = [];
    queue.push([rowIndex, colIndex]);
    while (queue.length > 0) {
        let position = queue.pop();
        let row = position[0];
        let col = position[1];
        binaryMatrix[row][col] = -1;
        //right
        if (col + 1 < binaryMatrix[0].length && binaryMatrix[row][col + 1] === 1) {
            queue.push([row, col + 1]);
        }

        //left
        if (col - 1 > 0 && binaryMatrix[row][col - 1] === 1) {
            queue.push([row, col - 1]);
        }

        //bottom
        if (row - 1 > 0 && binaryMatrix[row - 1][col] === 1) {
            queue.push([row - 1, col]);
        }

        //bottom
        if (row + 1 < binaryMatrix.length && binaryMatrix[row + 1][col] === 1) {
            queue.push([row + 1, col]);
        }
    }

    return binaryMatrix;
}

module.exports = countIsland;
