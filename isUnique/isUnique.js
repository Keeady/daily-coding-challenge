function isUnique(input) {
    var inputKey = input.trim();
    if (inputKey.length <= 1) {
        return true;
    }
    var charsFound = new Map();
    var inputArray = inputKey.split('');
    var index = 0;
    var currentChar;
    while (index < inputArray.length) {
        currentChar = inputArray[index].toLowerCase();
        currentChar = currentChar.trim();
        if (charsFound.has(currentChar)) {
            return false;
        }
        if (currentChar.length > 0) {
            charsFound.set(currentChar, 1);
        }
        index++;
    }
    return true;
}
module.exports = isUnique;
