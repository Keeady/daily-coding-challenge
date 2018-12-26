function findPalindromeSubstr(input) {
    var i;
    var output = [];
    for (i = 0; i < input.length; i++) {
        checkSubstr(input, i, 1, output);
    }
    return output;
}
function checkSubstr(input, start, length, output) {
    if (length > input.length / 2) {
        return output;
    }
    if (isPalindromeSub(input, start, length, length)) {
        output.push(input.substr(start, length * 2));
    }
    if (isPalindromeSub(input, start, length, length + 1)) {
        output.push(input.substr(start, length * 2 + 1));
    }
    checkSubstr(input, start, length + 1, output);
    return output;
}
function isPalindromeSub(input, start, leftSubLength, rightSubLength) {
    var left = start;
    var right = (start + leftSubLength) + rightSubLength - 1;
    while (left < right) {
        if (input.charAt(left) !== input.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
module.exports = findPalindromeSubstr;
