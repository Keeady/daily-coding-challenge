var TrieModule = require('../library/Trie');
var test = require('unit.js');
var TrieNodeModule = require('../library/TrieNode');

var trie = new TrieModule.Trie();
test.value(trie.getRoot().getValue()).is('*');
test.value(trie.getRoot().getChildren()).is(new Map());

trie.add('c');
var map = new Map();
map.set('c', new TrieNodeModule.TrieNode('c'));
test.value(trie.getRoot().getChildren()).is(map);
test.bool(trie.getRoot().has('c')).isTrue();
test.value(trie.getRoot().get('c')).is(new TrieNodeModule.TrieNode('c'));

trie.add('ca');
var cNode = trie.getRoot().get('c');
test.bool(cNode.has('a')).isTrue();
test.value(cNode.get('a')).is(new TrieNodeModule.TrieNode('a'));

trie.add('car');
var aNode = cNode.get('a');
test.bool(aNode.has('r')).isTrue();
test.value(aNode.get('r')).is(new TrieNodeModule.TrieNode('r'));

trie.add('nut');
test.bool(trie.getRoot().has('n')).isTrue();
test.value(trie.getRoot().get('n')).is(new TrieNodeModule.TrieNode('n'));

trie.add('cut');
test.bool(cNode.has('u')).isTrue();

trie.add('cap');
test.bool(aNode.has('p')).isTrue();
