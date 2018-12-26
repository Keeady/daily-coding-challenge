import {WordTrie} from "../library/WordTrie";

function findWordsMatrix(wordMatrix: Array<Array<String>>, wordList: Array<string>) {
    if (wordMatrix.length === 0 || wordList.length === 0) {
        return false;
    }

    let trie = buildWordTrie(wordMatrix);
    // on each cell
    // get all chars from the top, right, botttom, left starting from char
    // add chars in trie

    // iterate through word list
    //  for each word
            // split into array
            // find each char in trie

    return findWords(wordList, trie);
}

function buildWordTrie(wordMatrix) {
    let row, col = 0;
    let trie = new WordTrie();

    // iterate through matrix
    for (row = 0; row < wordMatrix.length; row++) {
        for (col = 0; col < wordMatrix[0].length; col++) {
            trie.addChars(getTopChars(row, col, wordMatrix));
            trie.addChars(getBottomChars(row, col, wordMatrix));
            trie.addChars(getLeftChars(row, col, wordMatrix));
            trie.addChars(getRightChars(row, col, wordMatrix));
        }
    }

    return trie;
}

function findWords(wordList, trie) {
    let words = {};
    let i;
    for (i = 0; i < wordList.length; i++) {
        let chars = wordList[i].split('');
        words[wordList[i]] = trie.findChars(chars);
    }

    return words;
}

function getTopChars(row, col, wordMatrix) {
    let chars = [];
    while(row >= 0) {
        chars.push(wordMatrix[row][col]);
        row--;
    }

    return chars;
}

function getBottomChars(row, col, wordMatrix) {
    let chars = [];
    while(row < wordMatrix.length) {
        chars.push(wordMatrix[row][col]);
        row++;
    }

    return chars;
}

/**
 * @param {number} row
 * @param {number} col
 * @param {string[][]} wordMatrix
 * @return {string[]}
 */
function getRightChars(row: number, col: number, wordMatrix: string[][]) {
    let chars = [];
    while(col < wordMatrix[0].length) {
        chars.push(wordMatrix[row][col]);
        col++;
    }

    return chars;
}

/**
 * @param {number} row
 * @param {number} col
 * @param {string[][]} wordMatrix
 * @return {string[]}
 */
function getLeftChars(row: number, col: number, wordMatrix: string[][]) {
    let chars = [];
    while(col >= 0) {
        chars.push(wordMatrix[row][col]);
        col--;
    }

    return chars;
}

module.exports = findWordsMatrix;
