function countIncorrectParentheses(input: string): number {
    let count = 0;
    let stack = [];
    let index = 0;
    let bracket;
    while (index < input.length) {
        bracket = input.charAt(index);
        if (isOpening(bracket)) {
            stack.push(bracket);
        } else {
            let prevBracket = stack.pop();
            if (isMatchingBracket(bracket, prevBracket) == false) {
                count += 1;
            }
        }

        index++;
    }

    count += stack.length;

    return count;
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

module.exports = countIncorrectParentheses;

