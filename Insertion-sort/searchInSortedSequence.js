function searchInSortedSequence(elements, value) {
    return search(elements, 0, elements.length - 1, value);
}
function search(elements, start, end, value) {
    if (start > end) {
        return null;
    }
    var midIndex = start + (end - start) / 2;
    midIndex = parseInt(midIndex.toString());
    if (value < elements[midIndex]) {
        return search(elements, start, midIndex - 1, value);
    }
    else if (value > elements[midIndex]) {
        return search(elements, midIndex + 1, end, value);
    }
    else {
        return midIndex;
    }
}
module.exports = searchInSortedSequence;
