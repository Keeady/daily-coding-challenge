function regexMatcher(input: string, pattern: string) {
    let patternIndex = 0;
    let stringIndex = 0;

    //if char pattern, match on char
    // -yes: inc pattern and string
    // -no: return false
    //if dot pattern, inc
    // if * pattern, dec pattern
     // -yes: inc string
    // -no: incr pattern twice
    return isMatch(input, pattern, patternIndex, stringIndex);
}

function isMatch(input: string, pattern: string, patternIndex: number, stringIndex: number) {
    //iterated over all patterns and string
    if (patternIndex >= pattern.length && stringIndex >= input.length) {
        return true;
    }

    if (patternIndex >= pattern.length) {
        return false;
    }

    let charPattern = pattern.charAt(patternIndex);
    if (stringIndex >= input.length) {
        if (charPattern === '*') {
            return isMatch(input, pattern, patternIndex + 1, stringIndex);
        } else if (patternIndex + 1 < pattern.length && pattern.charAt(patternIndex + 1) === '*') {
            return isMatch(input, pattern, patternIndex + 2, stringIndex);
        } else {
            return false;
        }
    }

    let charString = input.charAt(stringIndex);
    if (charPattern !== '*' && charPattern !== '.' && charPattern !== charString) {
        if (patternIndex + 1 < pattern.length && pattern.charAt(patternIndex + 1) === '*') {
            return isMatch(input, pattern, patternIndex + 2, stringIndex);
        }

        return false;
    }

    if (charPattern === '.') {
    }

    if (charPattern === '*') {
        return isMatch(input, pattern, patternIndex - 1, stringIndex);
    }

    return isMatch(input, pattern, patternIndex + 1, stringIndex + 1);
}

module.exports = regexMatcher;
