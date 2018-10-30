function searchInSortedSequence(elements: number[], value: number) {
    return search(elements, 0, elements.length - 1, value);
}

function search(elements: number[], start: number, end: number, value: number) {
    if (start > end) {
        return null;
    }

    let midIndex = start + (end - start) / 2;
    midIndex = parseInt(midIndex.toString());

    if (value < elements[midIndex]) {
        return search(elements, start, midIndex - 1, value);
    } else if (value > elements[midIndex]) {
        return search(elements, midIndex + 1, end, value);
    } else {
        return midIndex;
    }
}

module.exports = searchInSortedSequence;
