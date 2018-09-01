function sortPeaksAndValley(input: Array<number>) {
    let i = 0;
    for (i = 1; i < input.length - 1; i++) {
        if (input[i] < input[i - 1] && input[i] > input[i + 1] ||
            input[i] > input[i - 1] && input[i] < input[i + 1]
        ) {
            swap(input, i, i+1);
        }
    }

    return input;
}

function swap(input: Array<number>, left: number, right: number) {
    let buffer = input[left];
    input[left] = input[right];
    input[right] = buffer;

    return input;
}

module.exports = sortPeaksAndValley;
