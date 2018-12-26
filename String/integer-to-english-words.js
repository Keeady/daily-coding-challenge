function numberToWords(num) {
    var baseWords = new Map();
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
    var radixMap = new Map();
    radixMap.set(0, 'hundred');
    radixMap.set(2, 'thousand');
    radixMap.set(3, 'million');
    radixMap.set(4, 'billion');
    var input = Number(num).toString();
    var length = input.length;
    var i = length - 1;
    var digit;
    var output; // string english words
    var radix = 0;
    var outputGroups = [];
    var groupNumber = Math.ceil(length / 3);
    outputGroups = new Array(groupNumber);
    i = groupNumber;
    var startIndex = length - 3;
    startIndex = startIndex < 0 ? 0 : startIndex;
    var endIndex = length;
    var subLength = length - startIndex;
    while (i > 0) {
        outputGroups[i] = numberGroupToWords(input, startIndex, subLength, baseWords, radixMap);
        if (radixMap.has(radix + 1) && outputGroups[i].length > 0) {
            outputGroups[i].push(radixMap.get(radix + 1));
        }
        i--;
        radix++;
        var newStartIndex = startIndex - 3;
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
    var outputIndexStart = output.length - 2;
    var chars = input.substr(startIndex, 2);
    if (chars == '0' || chars === '00') {
        return [];
    }
    if (baseWords.has(chars)) {
        output[outputIndexStart] = baseWords.get(chars);
        return output;
    }
    var first = Number(parseInt(input.charAt(startIndex)) * 10).toString();
    var second = input.charAt(startIndex + 1);
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
    return outputArray.reduce(function (memo, out) {
        if (out && out.length > 0) {
            memo.push(out);
        }
        return memo;
    }, []);
}
function prettyPrint(outputArray) {
    var cleanOutput = outputArray.reduce(function (memo, out) {
        if (out && out.length > 0) {
            memo.push(out.join(' '));
        }
        return memo;
    }, []);
    return cleanOutput.join(' ');
}
function numberGroupToWords(input, startIndex, subLength, baseWords, radixMap) {
    var chars = input.substr(startIndex, subLength);
    var length = chars.length;
    var output;
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
