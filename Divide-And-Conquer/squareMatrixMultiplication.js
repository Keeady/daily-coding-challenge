function multiplySquareMatrices(left, right) {
    var row = 0;
    var col = 0;
    var i = 0;
    var result = [];
    while (row < left.length) {
        col = 0;
        result[row] = [];
        while (col < right.length) {
            var total = 0;
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
