function isUniqueExtended(input) {
    let inputKey = input.trim();
    if (inputKey.length <= 1) {
        return true;
    }

    let charsFound = [];
    let inputArray = inputKey.split('');
    let index = 0;
    let currentChar;

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
