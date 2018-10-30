function removeDuplicates(elements) {
    var elementMap = new Map();
    var uniqueElements = [];
    var index = 0;
    while (index < elements.length) {
        if (elementMap.has(elements[index]) === false) {
            elementMap.set(elements[index], true);
        }
        index++;
    }
    elementMap.forEach(function (value, key) {
        uniqueElements.push(key);
    });
    return uniqueElements;
}
module.exports = removeDuplicates;
