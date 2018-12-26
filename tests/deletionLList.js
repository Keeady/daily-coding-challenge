var test = require('unit.js');
var linkedList = require('../List/deletionLinkedList');
var linkedNode = require('../library/LinkedNode');

var llist = new linkedList.DeletionLinkedList();

var single = llist.add(1);
test.value(llist.getHead().data).is(1);
test.value(llist.getTail().data).is(1);
var result = llist.deleteNode(single);
test.value(llist.getHead()).isNull();
test.value(llist.getTail()).isNull();

result = llist.deleteNode(single);
test.value(result).isNull();

var randomNode = new linkedNode.LinkedNode(12);
result = llist.deleteNode(randomNode);
test.value(result).isNull();

llist.add(11);
result = llist.deleteNode(randomNode);
test.object(result).is(llist.getHead());
test.value(llist.getHead().data).is(11);

//2 elements deletion of tail
var three = llist.add(3);
llist.deleteNode(three);
test.value(llist.getHead().data).is(11);
test.value(llist.getTail().data).is(11);

//3 elements deletion of middle
var four = llist.add(4);
var five = llist.add(5);
llist.deleteNode(four);
test.value(llist.getHead().data).is(11);
test.value(llist.getTail().data).is(5);
test.object(llist.getHead().next).is(five);

/*
var four2 = llist.add(4);
test.value(llist.getHead().data).is(3);
//test.value(llist.getTail().data).is(5);

var six = llist.insertAfter(three, 6);
test.value(llist.getHead().next.data).is(6);
test.value(six.next.data).is(four.data);

console.log(six);
console.log(five);
llist.deleteNode(four);
//test.value(six.next.data).is(five.data);

/*llist.deleteNode(five);
test.value(four.next).isNull();
test.value(llist.getTail().data).is(4);

llist.deleteNode(three);
test.value(llist.getHead().data).is(6);*/


