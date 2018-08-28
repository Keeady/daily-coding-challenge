function isUnique(input: string) {
    let inputKey = input.trim();
    if (inputKey.length <= 1) {
        return true;
    }

    let charsFound = new Map();
    let inputArray = inputKey.split('');
    let index = 0;
    let currentChar;

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
