function findPairsWithGivenDifference(inputArray, k) {
    let yTable = new Map();
    let index;
    let results;

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
    let value;
    if (x > y) {
        value = yTable.get(y);
        value.push(x);
        yTable.set(y, value);
    } else {
        value = yTable.get(x);
        value.push(y);
        yTable.set(x, value);
    }
    return yTable;
}

function buildPairs(yTable) {
    let results = [];
    let index;

    yTable.forEach(function(values, key) {
        for (index = 0; index < values.length; index++) {
            results.push([values[index], key]);
        }
    });

    return results;
}

function findPairs(inputArray, inputTable, k) {
    let results = [];
    //k = 10
    // 12, 5, 2, 15, 25
    //12 => [], 5 => [], 2 => [], 15 => [], 25 => []
    //12+10 = 22
    //5 + 10 = 15
    //2 + 10 = 12
    //15 + 10 = 25
    //25 + 10 = 35
    inputTable.forEach( (value, key) => {
        let right = key + k;

        if (inputTable.has(right)) {
            results.push([right, key]);
        }
    });

    return results;
}

function findPairsSlow(inputArray, yTable, k) {
    let index;

    for (index = 0; index < inputArray.length - 1; index++) {
        let nextIndex = index + 1;
        for (nextIndex = index + 1; nextIndex < inputArray.length; nextIndex++) {
            let diff = inputArray[index] - inputArray[nextIndex];
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
