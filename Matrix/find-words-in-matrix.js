"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var WordTrie_1 = require("../library/WordTrie");
function findWordsMatrix(wordMatrix, wordList) {
    if (wordMatrix.length === 0 || wordList.length === 0) {
        return false;
    }
    var trie = buildWordTrie(wordMatrix);
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
    var row, col = 0;
    var trie = new WordTrie_1.WordTrie();
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
    var words = {};
    var i;
    for (i = 0; i < wordList.length; i++) {
        var chars = wordList[i].split('');
        words[wordList[i]] = trie.findChars(chars);
    }
    return words;
}
function getTopChars(row, col, wordMatrix) {
    var chars = [];
    while (row >= 0) {
        chars.push(wordMatrix[row][col]);
        row--;
    }
    return chars;
}
function getBottomChars(row, col, wordMatrix) {
    var chars = [];
    while (row < wordMatrix.length) {
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
function getRightChars(row, col, wordMatrix) {
    var chars = [];
    while (col < wordMatrix[0].length) {
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
function getLeftChars(row, col, wordMatrix) {
    var chars = [];
    while (col >= 0) {
        chars.push(wordMatrix[row][col]);
        col--;
    }
    return chars;
}
module.exports = findWordsMatrix;
