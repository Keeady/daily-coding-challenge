function binaryInsertionSortElements(elements: number[]) {
    let j = 1;
    while (j < elements.length) {
        let i = j - 1;
        let key = elements[j];
        let index = binarySearch(elements, 0, i, key);
        let start = index + 1;
        while (i >= start) {
            elements[i + 1] = elements[i];
            i--;
        }

        elements[index + 1] = key;
        j++;
    }
}

function binarySearch(elements: number[], start: number, end: number, value: number) {
    if (start > end) {
        return end;
    }

    let midIndex = Math.floor(start + (end - start) / 2);

    if (value < elements[midIndex]) {
        return binarySearch(elements, start, midIndex - 1, value);
    } else if (value > elements[midIndex]) {
        return binarySearch(elements, midIndex + 1, end, value);
    } else {
        return midIndex;
    }
}

module.exports = binaryInsertionSortElements;
