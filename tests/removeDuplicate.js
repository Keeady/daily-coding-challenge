var removeDuplicate = require('../Remove-Dups/removeDuplicate');
var test = require('unit.js');
var LinkedNodeModule = require( "../library/LinkedNode.js");
var LinkedListModule = require('../Library/LinkedList.js');

var llist = new LinkedListModule.LinkedList();
llist.add(1);
llist.add(2);
llist.add(2);
var head = removeDuplicate(llist.head);
test.value(head.next.next).is(null);

llist = new LinkedListModule.LinkedList();
llist.add(1);
llist.add(2);
llist.add(2);
llist.add(3);

head = removeDuplicate(llist.head);
test.object(head.next.next).isNotEmpty();
test.value(head.next.next.data).is(3);
