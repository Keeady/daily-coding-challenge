var add = require('../List/add-two-numbers');
var test = require('unit.js');
var linkedNode = require('../library/LinkedNode');

var two = new linkedNode.LinkedNode(2);
var four = new linkedNode.LinkedNode(4);
var eight = new linkedNode.LinkedNode(8);
var five = new linkedNode.LinkedNode(5);
var six = new linkedNode.LinkedNode(6);

//2->4->8
two.next = four;
four.next = eight;
//5->6->4
five.next = six;
six.next = new linkedNode.LinkedNode(4);

var res = add(two, five);

test.value(res.data).is(7);
test.value(res.next.data).is(0);
test.value(res.next.next.data).is(3);
test.value(res.next.next.next.data).is(1);
