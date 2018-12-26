var test = require('unit.js');
var module = require('../List/find-llist-intersection');
var listNode = module.ListNode;
var find = module.findIntersection;

var four = new listNode(4);
var one = new listNode(1);
var eight = new listNode(8);
four.next = one;
one.next = eight;
var five = new listNode(5);
var zero = new listNode(0);
five.next = zero;
var one2 = new listNode(1);
zero.next = one2;
one2.next = eight;
eight.next = new listNode(4, new listNode(5));
var res = find(four, five);
test.value(res.val).is(1);


one.next = new listNode(7, eight);
one2.next = new listNode(6, eight);
res = find(four, five);
test.value(res.val).is(8);


one.next = new listNode(7, eight);
one2.next = eight;
res = find(four, five);
test.value(res.val).is(8);


one2.next = new listNode(9, new listNode(10, new listNode(11)));
res = find(four, five);
test.value(res).isNull();

