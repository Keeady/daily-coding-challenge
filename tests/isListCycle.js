var linkedNode = require("../library/LinkedNode");

var test = require('unit.js');
var isCycle = require('../List/IsListCycle');

var head = new linkedNode.LinkedNode(0);
var one = new linkedNode.LinkedNode(1);
var two = new linkedNode.LinkedNode(2);
var three = new linkedNode.LinkedNode(3);
var four = new linkedNode.LinkedNode(4);

head.next = one;
one.next = two;
two.next = three;
three.next = four;
four.next = one;

var result = isCycle(head);
test.bool(result).isTrue();

four.next = null;
result = isCycle(head);
test.bool(result).isFalse();
