function longestPalindromeSubstr(input) {
    let i;
    let output = '';

    if (input.length <= 1) {
        return input;
    }

    for (i = 0; i < input.length; i++) {
        let currentOutput = checkPalindromeSub(input, i, 1, output);
        if (currentOutput.length > output.length) {
            output = currentOutput;
        }
    }

    return output;
}

function checkPalindromeSub(input, start, length, output) {
    if (length > input.length / 2) {
        return output;
    }

    if (length === 1 && output.length < length) {
        output = input.substr(start, length);
    }

    if (isPalindromeSeq(input, start, length, length) && output.length < start + length * 2) {
        output = input.substr(start, length * 2);
    }

    if (isPalindromeSeq(input, start, length, length + 1) && output.length < start + length * 2 + 1) {
        output = input.substr(start, length * 2 + 1);
    }

    return checkPalindromeSub(input, start, length + 1, output);
}

function isPalindromeSeq(input, start, leftSubLength, rightSubLength) {
    let left = start;
    let right = start + leftSubLength + rightSubLength - 1;
    while (left < right) {
        if (input.charAt(left) !== input.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

module.exports = longestPalindromeSubstr;
