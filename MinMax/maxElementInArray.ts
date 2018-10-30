function findMaxElement(input: number[]) {
    let max = 0;
    if (input.length == 0) {
        return null;
    }

    max = input[0];
    let i;
    for (i = 0; i < input.length; i++) {
        if (input[i] > max) {
            max = input[i];
        }
    }

    return max;
}

module.exports = findMaxElement;
