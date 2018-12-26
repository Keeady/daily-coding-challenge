var test = require('unit.js');
var wordTrie = require('../library/WordTrie');

//a g i w t
//x l o a s
//i o n t i
//s w e l l
var chars = ['s', 'w', 'e', 'l', 'l'];
var trie = new wordTrie.WordTrie();
trie.addChars(chars);
test.object(trie.getRoot()).isNotEmpty();
test.bool(trie.getRoot().has('s')).isTrue();
var s = trie.getRoot().get('s');
test.bool(s.has('w')).isTrue();
var w = s.get('w');
test.bool(w.has('e')).isTrue();
var e = w.get('e');
test.bool(e.has('l')).isTrue();
var l = e.get('l');
test.bool(l.has('l')).isTrue();
var l2 = l.get('l');
test.value(l2.getChildren()).isEmpty();

trie.addChars([ 'w', 'e', 'l', 'l']);

var found = trie.findChars(['s','w','e','l','l']);
test.bool(found).isTrue();
found = trie.findChars(['w','e','l','l']);
test.bool(found).isTrue();
found = trie.findChars(['s','w','e']);
test.bool(found).isTrue();
found = trie.findChars(['w','e']);
test.bool(found).isTrue();
found = trie.findChars(['s','w','e','l','t']);
test.bool(found).isFalse();
found = trie.findChars(['w','e','l','l','s']);
test.bool(found).isFalse();
found = trie.findChars(['h','e','l','l']);
test.bool(found).isFalse();
