function searchInSequence(elements: number[], value: number) {
    let i = 0;
    while (i < elements.length) {
        if (elements[i] === value) {
            return i;
        }

        i++;
    }

    return null;
}

module.exports = searchInSequence;
