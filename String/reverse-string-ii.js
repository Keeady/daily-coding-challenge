function reversek(input, k) {
    //split to array of chars
    var chars = input.split('');
    var i = 0;
    var n = chars.length;
    while (i < n) {
        if (i + 2 * k < n) {
            reverseChars(chars, i, i + k);
            i += 2 * k;
        }
        else if (i + k < n) {
            reverseChars(chars, i, i + k);
            i = n;
        }
        else {
            reverseChars(chars, i, n);
            i = n;
        }
    }
    return chars.join('');
}
function reverseChars(chars, start, end) {
    var left = start;
    var right = end - 1;
    var buffer;
    while (left < right) {
        buffer = chars[left];
        chars[left] = chars[right];
        chars[right] = buffer;
        left++;
        right--;
    }
    return chars;
}
module.exports = reversek;
