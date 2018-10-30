var test = require('unit.js');
var findMth = require('../List/MthElement');
var linkedList = require('../library/LinkedList');
//no element
var llist = new linkedList.LinkedList();
var result = findMth(null, 5);
test.value(result).isNull();

//1 element
var single = llist.add(1);
result = findMth(llist.getHead(), 0);
test.object(result).is(single);

//2 element
var two = llist.add(2);
result = findMth(llist.getHead(), 0);
test.object(result).is(two);

result = findMth(llist.getHead(), 1);
test.object(result).is(single);

//5 elements
var three = llist.add(3);
var four = llist.add(4);
var five = llist.add(5);

result = findMth(llist.getHead(), 0);
test.object(result).is(five);

result = findMth(llist.getHead(), 1);
test.object(result).is(four);

result = findMth(llist.getHead(), 2);
test.object(result).is(three);

result = findMth(llist.getHead(), 3);
test.object(result).is(two);

result = findMth(llist.getHead(), 4);
test.object(result).is(single);
