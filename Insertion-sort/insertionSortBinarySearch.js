function binaryInsertionSortElements(elements) {
    var j = 1;
    while (j < elements.length) {
        var i = j - 1;
        var key = elements[j];
        var index = binarySearch(elements, 0, i, key);
        var start = index + 1;
        while (i >= start) {
            elements[i + 1] = elements[i];
            i--;
        }
        elements[index + 1] = key;
        j++;
    }
}
function binarySearch(elements, start, end, value) {
    if (start > end) {
        return end;
    }
    var midIndex = Math.floor(start + (end - start) / 2);
    if (value < elements[midIndex]) {
        return binarySearch(elements, start, midIndex - 1, value);
    }
    else if (value > elements[midIndex]) {
        return binarySearch(elements, midIndex + 1, end, value);
    }
    else {
        return midIndex;
    }
}
module.exports = binaryInsertionSortElements;
