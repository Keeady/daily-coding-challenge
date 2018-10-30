function reverse(input: string): string {
    let left = 0;
    let right = input.length - 1;
    let buffer;
    let inputArray = input.split('');

    while (left < right) {
        buffer = inputArray[left];
        inputArray[left] = inputArray[right];
        inputArray[right] = buffer;
        left++;
        right--;
    }

    return inputArray.join('');
}

module.exports = reverse;
