function countIncorrectParentheses(input) {
    var count = 0;
    var stack = [];
    var index = 0;
    var bracket;
    while (index < input.length) {
        bracket = input.charAt(index);
        if (isOpening(bracket)) {
            stack.push(bracket);
        }
        else {
            var prevBracket = stack.pop();
            if (isMatchingBracket(bracket, prevBracket) == false) {
                count += 1;
            }
        }
        index++;
    }
    count += stack.length;
    return count;
}
function isOpening(bracket) {
    return (bracket == '{' || bracket == '[' || bracket == '(');
}
function isMatchingBracket(bracket, previousBracket) {
    var match;
    switch (bracket) {
        case '}':
            match = '{';
            break;
        case ')':
            match = '(';
            break;
        case ']':
            match = '[';
            break;
        default:
            throw 'Invalid bracket';
    }
    return (match === previousBracket);
}
module.exports = countIncorrectParentheses;
