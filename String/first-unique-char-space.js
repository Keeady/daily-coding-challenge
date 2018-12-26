function findFirstUniqueCharacterSpaceOptimized(letter) {
    //split into array of chars
    var chars = letter.split('');
    //char:[index,count] store for letter and index,count
    var letterMap = buildLetterMap(chars);
    return findUniqueChar(letterMap);
}
function buildLetterMap(chars) {
    var letterMap = new Map();
    var i;
    var entry;
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
    var index = -1;
    var iterator = letterMap.values();
    var entry = iterator.next();
    while (!entry.done && index < 0) {
        var value = entry.value;
        if (value[1] === 1) {
            index = value[0];
        }
        entry = iterator.next();
    }
    return index;
}
module.exports = findFirstUniqueCharacterSpaceOptimized;
