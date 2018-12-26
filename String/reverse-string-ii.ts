function reversek(input, k) {
    //split to array of chars
    let chars = input.split('');
    let i = 0;
    let n = chars.length;

    while (i < n) {
        if (i + 2 * k < n) {
            reverseChars(chars, i, i + k);
            i += 2 * k;
        } else if (i + k < n) {
            reverseChars(chars, i, i + k);
            i = n;
        } else {
            reverseChars(chars, i, n);
            i = n;
        }
    }

    return chars.join('');
}

function reverseChars(chars, start, end) {
    let left = start;
    let right = end - 1;
    let buffer;

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
