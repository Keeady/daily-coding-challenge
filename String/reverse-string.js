function reverse(input) {
    var left = 0;
    var right = input.length - 1;
    var buffer;
    var inputArray = input.split('');
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
