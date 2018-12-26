function isPalindrome(input) {
    var left = 0;
    var right = input.length - 1;
    while (left < right) {
        if (input.charAt(left) !== input.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
module.exports = isPalindrome;
