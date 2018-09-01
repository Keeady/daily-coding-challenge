var LinkedNodeModule = require( "../library/LinkedNode.js");
var test = require('unit.js');
var linkedListModule = require('../Library/LinkedList.js');
var llist = new linkedListModule.LinkedList();
llist.add(1);

test.object(llist.head).isNotEmpty();
test.object(llist.head).match(new LinkedNodeModule.LinkedNode(1, null, null));

llist.add(1);
test.value(llist.head.data).is(1);
test.value(llist.head.next.data).is(1);
test.value(llist.head.next.next).is(null);

llist.add(2);
test.object(llist.head.next).isNotEmpty();
var next = new LinkedNodeModule.LinkedNode(2, null, null);
test.object(llist.head).match(new LinkedNodeModule.LinkedNode(1, next, null));
test.object(llist.head.next).match(next);

llist = new linkedListModule.LinkedList();
llist.add(1);
llist.add(2);
llist.add(3);
llist.add(4);
llist.remove(2);
next = new LinkedNodeModule.LinkedNode(3, null, null);
test.object(llist.head.next).match(next);

llist.remove(1);
test.object(llist.head).isNotEmpty();
test.object(llist.head).match(next);

llist.remove(4);
test.value(llist.head.next).is(null);

llist.remove(3);
test.value(llist.head).is(null);
