var test = require('unit.js');
var linkedList = require('../List/deletionLinkedList');
var linkedNode = require('../library/LinkedNode');

var llist = new linkedList.DeletionLinkedList();
//insert no element
var five = llist.insertAfter(null, 5);
test.value(llist.getHead().data).is(5);
test.value(llist.getTail().data).is(5);

//insert in 1  element list
var six = llist.insertAfter(five, 6);
test.value(llist.getHead().data).is(5);
test.value(llist.getTail().data).is(6);

//insert in the middle
var fivefive = llist.insertAfter(five, 5.5);
test.value(llist.getHead().data).is(5);
test.value(llist.getTail().data).is(6);
test.object(fivefive).is(llist.getHead().next);
test.object(llist.getTail()).is(fivefive.next);

//insert at the end
var seven = llist.insertAfter(six, 7);
test.value(llist.getHead().data).is(5);
test.value(llist.getTail().data).is(7);
test.object(llist.getTail()).is(six.next);
