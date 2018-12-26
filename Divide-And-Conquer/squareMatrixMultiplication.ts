function multiplySquareMatrices(left: number[][], right: number[][]) {
    let row = 0;
    let col = 0;
    let i = 0;
    let result: number[][] = [];

    while (row < left.length) {
        col = 0;
        result[row] = [];
        while (col < right.length) {
            let total = 0;
            i = 0;
            while (i < right.length) {
                total += left[row][i] * right[i][col];
                i++;
            }

            result[row][col] = total;
            col++;
        }

        row++;
    }

    return result;
}

module.exports = multiplySquareMatrices;
