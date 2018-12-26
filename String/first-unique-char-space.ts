
function findFirstUniqueCharacterSpaceOptimized(letter) {
    //split into array of chars
    const chars = letter.split('');
    //char:[index,count] store for letter and index,count
    let letterMap = buildLetterMap(chars);
    return findUniqueChar(letterMap);
}

function buildLetterMap(chars) {
    let letterMap = new Map<String, Array<Number>>();
    let i;
    let entry;

    for (i = 0; i < chars.length; i++) {
        entry = [i, 0];
        if (letterMap.has(chars[i])) {
            entry = letterMap.get(chars[i]);
        }

        entry[1] += 1;

        letterMap.set(chars[i], entry);
    }

    return letterMap;
}

function findUniqueChar(letterMap) {
    let index = -1;
    let iterator = letterMap.values();
    let entry = iterator.next();

    while (!entry.done && index < 0) {
        let value = entry.value;
        if (value[1] === 1) {
            index = value[0];
        }

        entry = iterator.next();
    }

    return index;
}

module.exports = findFirstUniqueCharacterSpaceOptimized;
