function numberToWords(num) {
    let baseWords = new Map();
    baseWords.set('0', 'zero');
    baseWords.set('1', 'one');
    baseWords.set('2', 'two');
    baseWords.set('3', 'three');
    baseWords.set('4', 'four');
    baseWords.set('5', 'five');
    baseWords.set('7', 'seven');
    baseWords.set('8', 'eight');
    baseWords.set('11', 'eleven');
    baseWords.set('12', 'twelve');
    baseWords.set('13', 'thirteen');
    baseWords.set('10', 'ten');
    baseWords.set('20', 'twenty');
    baseWords.set('30', 'thirty');
    baseWords.set('40', 'forty');
    baseWords.set('60', 'sixty');
    baseWords.set('90', 'ninety');

    let radixMap = new Map();
    radixMap.set(0, 'hundred');
    radixMap.set(2, 'thousand');
    radixMap.set(3, 'million');
    radixMap.set(4, 'billion');

    let input = Number(num).toString();
    let length = input.length;
    let i = length - 1;
    let digit;
    let output; // string english words
    let radix = 0;
    let outputGroups = [];

    let groupNumber = Math.ceil(length / 3);
    outputGroups = new Array(groupNumber);
    i = groupNumber;
    let startIndex = length - 3;
    startIndex = startIndex < 0 ? 0 : startIndex;
    let endIndex = length;
    let subLength = length - startIndex;
    while (i > 0) {
        outputGroups[i] = numberGroupToWords(input, startIndex, subLength, baseWords, radixMap);
        if (radixMap.has(radix + 1) && outputGroups[i].length > 0) {
            outputGroups[i].push(radixMap.get(radix + 1));
        }

        i--;
        radix++;
        let newStartIndex = startIndex - 3;
        newStartIndex = newStartIndex < 0 ? 0 : newStartIndex;
        subLength = startIndex - newStartIndex;
        startIndex = newStartIndex;
    }

    return prettyPrint(outputGroups);
}

/**
 *
 * @param baseWords
 * @param input string of 3 digits or less
 * @param output
 * @return {any}
 */
function twoDigitsToWords(baseWords, input, startIndex, output) {
    let outputIndexStart = output.length - 2;
    let chars = input.substr(startIndex, 2);

    if (chars == '0'  || chars === '00') {
        return [];
    }

    if (baseWords.has(chars)) {
        output[outputIndexStart] = baseWords.get(chars);
        return output;
    }

    let first = Number(parseInt(input.charAt(startIndex)) * 10).toString();
    let second = input.charAt(startIndex + 1);
    if (first !== '0') {
        output[outputIndexStart] = baseWords.get(first);
    }

    if (second !== '0') {
        output[outputIndexStart + 1] = baseWords.get(second);
    }
    return output;
}

function threeDigitsToWords(baseWords, radixMap, input, startIndex, output) {
    output = twoDigitsToWords(baseWords, input, 1, output);
    if (input.charAt(0) === '0') {
        return output;
    }

    output[0] = baseWords.get(input.charAt(0));
    output[1] = radixMap.get(0);

    return output;
}

function print(outputArray) {
    return outputArray.reduce((memo, out: any) => {
        if (out && out.length > 0) {
            memo.push(out);
        }

        return memo;
    }, []);
}

function prettyPrint(outputArray) {
    let cleanOutput = outputArray.reduce((memo, out: any) => {
        if (out && out.length > 0) {
            memo.push(out.join(' '));
        }

        return memo;
    }, []);

    return cleanOutput.join(' ');
}

function numberGroupToWords(input, startIndex, subLength, baseWords, radixMap) {
    let chars = input.substr(startIndex, subLength);
    let length = chars.length;
    let output;

    if (length === 1) {
        return [baseWords.get(chars)];
    }

    if (length === 2) {
        output = new Array(2);
        output = twoDigitsToWords(baseWords, chars, 0, output);
        return print(output);
    }

    if (length === 3) {
        output = new Array(4);
        output = threeDigitsToWords(baseWords, radixMap, chars, 1, output);
        return print(output);
    }
}

module.exports = numberToWords;
