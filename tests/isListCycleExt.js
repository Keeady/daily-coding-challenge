var linkedNode = require("../library/LinkedNode");

var test = require('unit.js');
var isCycle = require('../List/isListCycleExtended');

var head = new linkedNode.LinkedNode(0);
var result = isCycle(head);
test.bool(result).isFalse();

var one = new linkedNode.LinkedNode(1);
head.next = one;
result = isCycle(head);
test.bool(result).isFalse();

one.next = head;
result = isCycle(head);
test.bool(result).isTrue();

var two = new linkedNode.LinkedNode(2);
var three = new linkedNode.LinkedNode(3);

one.next = two;
two.next = three;
three.next = head;
var result = isCycle(head);
test.bool(result).isTrue();

var four = new linkedNode.LinkedNode(4);
three.next = four;
four.next = two;

var result = isCycle(head);
test.bool(result).isTrue();

four.next = null;
result = isCycle(head);
test.bool(result).isFalse();

