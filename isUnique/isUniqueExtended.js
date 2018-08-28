function isUniqueExtended(input) {
    var inputKey = input.trim();
    if (inputKey.length <= 1) {
        return true;
    }
    var charsFound = [];
    var inputArray = inputKey.split('');
    var index = 0;
    var currentChar;
    while (index < inputArray.length) {
        currentChar = inputArray[index].toLowerCase();
        currentChar = currentChar.trim();
        if (currentChar.length > 0) {
            currentChar = currentChar.charCodeAt(0);
            if (charsFound[currentChar] == 1) {
                return false;
            }
            charsFound[currentChar] = 1;
        }
        index++;
    }
    return true;
}
module.exports = isUniqueExtended;
