function removeDuplicates(elements: number[]) {
    let elementMap = new Map<number, boolean>();
    let index = 0;
    while (index < elements.length) {
        if (elementMap.has(elements[index])) {
            elements.splice(index, 1);
        } else {
            elementMap.set(elements[index], true);
            index++;
        }
    }

    return elements;
}

module.exports = removeDuplicates;
