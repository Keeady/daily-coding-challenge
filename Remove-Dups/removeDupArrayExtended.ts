function removeDuplicates(elements: number[]) {
    let elementMap = new Map<number, boolean>();
    let uniqueElements = [];
    let index = 0;
    while (index < elements.length) {
        if (elementMap.has(elements[index]) === false) {
            elementMap.set(elements[index], true);
        }

        index++;
    }

    elementMap.forEach((value, key) => {
        uniqueElements.push(key);
    });

    return uniqueElements;
}

module.exports = removeDuplicates;
