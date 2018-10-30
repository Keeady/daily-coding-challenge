function sortNonIncrementElement(elements) {
    var j = 1;
    var i;
    var key;
    while (j < elements.length) {
        i = j - 1;
        key = elements[j];
        while (i >= 0 && elements[i] < key) {
            elements[i + 1] = elements[i];
            i--;
        }
        elements[i + 1] = key;
        j++;
    }
}
module.exports = sortNonIncrementElement;
