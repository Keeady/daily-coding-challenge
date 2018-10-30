function sortElements(elements: number[]) {
    let j = 1;
    let i;
    let key;
    while (j < elements.length) {
        i = j - 1;
        key = elements[j];
        while (i >= 0 && elements[i] > key) {
            elements[i + 1] = elements[i];
            i--;
        }

        elements[i + 1] = key;
        j++;
    }

    return elements;
}

module.exports = sortElements;
