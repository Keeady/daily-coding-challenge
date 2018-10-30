function checkNestedParentheses(input) {
    var stack = [];
    var index = 0;
    var bracket;
    while (index < input.length) {
        bracket = input.charAt(index);
        if (isOpening(bracket)) {
            stack.push(bracket);
        }
        else {
            if (stack.length <= 0 || isMatchingBracket(bracket, stack.pop()) == false) {
                return false;
            }
        }
        index++;
    }
    return (stack.length == 0);
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
module.exports = checkNestedParentheses;
