//leetcode
//['l','e','e','t','c','o','d','e']
//[l->0, e->-1, t->3, c->4, o->5
//[l,t,c,o

//1->2


function findFirstUniqueCharacter(letter) {
    //split into array of chars
    const chars = letter.split('');
    //key:value store for letter and index
    let letterMap = new Map<String, Number>();
    //queue to keep keys in order
    let queue = [];

    let i;
    for (i = 0; i < chars.length; i++) {
        if (letterMap.has(chars[i])) {
            letterMap.set(chars[i], -1);
        } else {
            letterMap.set(chars[i], i);
            queue.push(chars[i]);
        }
    }

    return findUniqueChar(letterMap, queue);
}

function findUniqueChar(letterMap, queue) {
    let char;
    while (queue.length > 0) {
        char = queue.shift();
        if (letterMap.has(char) && letterMap.get(char) >= 0) {
            return letterMap.get(char);
        }
    }

    return -1;
}

module.exports = findFirstUniqueCharacter;
