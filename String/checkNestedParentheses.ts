function checkNestedParentheses(input: string): boolean {
    let stack = [];
    let index = 0;
    let bracket;
    while (index < input.length) {
        bracket = input.charAt(index);
        if (isOpening(bracket)) {
            stack.push(bracket);
        } else {
            if (stack.length <= 0 || isMatchingBracket(bracket, stack.pop()) == false) {
                return false;
            }
        }
        index++;
    }

    return (stack.length == 0);
}

function isOpening(bracket: string): boolean {
    return (bracket == '{' || bracket == '[' || bracket == '(');
}

function isMatchingBracket(bracket: string, previousBracket: string): boolean {
    let match;
    switch(bracket) {
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
