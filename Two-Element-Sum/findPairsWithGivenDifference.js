function findPairsWithGivenDifference(inputArray, k) {
    var yTable = new Map();
    var index;
    var results;
    // create a hashtable with y as keys from the original array
    for (index = 0; index < inputArray.length; index++) {
        yTable.set(inputArray[index], []);
    }
    // sort
    //inputArray.sort();
    // add x as values in hashtable
    //yTable = findPairsSlow(inputArray, yTable, k);
    // build x,y pairs from hashtable
    //let results = buildPairs(yTable);
    results = findPairs(inputArray, yTable, k);
    return results;
}
function buildTable(yTable, x, y) {
    var value;
    if (x > y) {
        value = yTable.get(y);
        value.push(x);
        yTable.set(y, value);
    }
    else {
        value = yTable.get(x);
        value.push(y);
        yTable.set(x, value);
    }
    return yTable;
}
function buildPairs(yTable) {
    var results = [];
    var index;
    yTable.forEach(function (values, key) {
        for (index = 0; index < values.length; index++) {
            results.push([values[index], key]);
        }
    });
    return results;
}
function findPairs(inputArray, inputTable, k) {
    var results = [];
    //k = 10
    // 12, 5, 2, 15, 25
    //12 => [], 5 => [], 2 => [], 15 => [], 25 => []
    //12+10 = 22
    //5 + 10 = 15
    //2 + 10 = 12
    //15 + 10 = 25
    //25 + 10 = 35
    inputTable.forEach(function (value, key) {
        var right = key + k;
        if (inputTable.has(right)) {
            results.push([right, key]);
        }
    });
    return results;
}
function findPairsSlow(inputArray, yTable, k) {
    var index;
    for (index = 0; index < inputArray.length - 1; index++) {
        var nextIndex = index + 1;
        for (nextIndex = index + 1; nextIndex < inputArray.length; nextIndex++) {
            var diff = inputArray[index] - inputArray[nextIndex];
            if (Math.abs(diff) > k) {
                break;
            }
            if (Math.abs(diff) == k) {
                yTable = buildTable(yTable, inputArray[index], inputArray[nextIndex]);
            }
        }
    }
    return yTable;
}
module.exports = findPairsWithGivenDifference;
