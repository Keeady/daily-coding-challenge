function sortElements(elements: number[]) {
    let num = elements.length;
    return sortRecursively(elements, num);
}

function sortRecursively(elements: number[], index: number) {
    if (index > 1) {
        index -= 1;
        sortRecursively(elements, index);
    }

    //insert num in elements
    return insertionSort(elements, 0, index, elements[index]);
}

function insertionSort(elements: number[], start: number, end: number, num: number) {
    let i = end - 1;
    while (i >= start && i < end && elements[i] > num) {
        elements[i + 1] = elements[i];
        i--;
    }
    elements[i + 1] = num;

    return elements;
}

module.exports = sortElements;
