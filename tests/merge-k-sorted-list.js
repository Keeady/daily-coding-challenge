var test = require('unit.js');
var module = require('../List/merge-k-sorted-list');
var merge = module.mergeKSortedList;
var listNode = module.ListNode;

function print(head) {
    var list = [];
    while (head != null) {
        list.push(head.val);
        head = head.next;
    }

    return list;
}

var one = new listNode(1, new listNode(2, new listNode(3)));
var five = new listNode(5, new listNode(10, new listNode(15, new listNode(34))));
var four = new listNode(4, new listNode(5, new listNode(6)));

var res = merge([one]);
res = print(res);
test.value(res).is([1,2,3]);

one = new listNode(1, new listNode(2, new listNode(3)));
five = new listNode(5, new listNode(10, new listNode(15, new listNode(34))));
four = new listNode(4, new listNode(5, new listNode(6)));


res = merge([one, five, four]);
res = print(res);
test.value(res).is([1,2,3,4,5,5,6,10,15,34]);

one = new listNode(1, new listNode(2, new listNode(3)));
five = new listNode(5, new listNode(10, new listNode(15, new listNode(34))));
four = new listNode(4, new listNode(5, new listNode(6)));

res = merge([four, five, one]);
res = print(res);

test.value(res).is([1,2,3,4,5,5,6,10,15,34]);

res = merge([null, null]);
test.value(res).is(null);

one = new listNode(5, new listNode(6, new listNode(34)));
five = new listNode(1, new listNode(4, new listNode(5, new listNode(10))));
four = new listNode(2, new listNode(3, new listNode(15)));

res = merge([four, five, one]);
res = print(res);
test.value(res).is([1,2,3,4,5,5,6,10,15,34]);

one = new listNode(5, new listNode(5, new listNode(34)));
five = new listNode(1, new listNode(4, new listNode(5, new listNode(5))));
four = new listNode(2, new listNode(15, new listNode(15)));

res = merge([four, five, one]);
res = print(res);
test.value(res).is([1,2,4,5,5,5,5,15,15,34]);

one = new listNode(-5, new listNode(-5, new listNode(3)));
five = new listNode(-15, new listNode(-4, new listNode(5, new listNode(5))));
four = new listNode(2, new listNode(15, new listNode(15)));

res = merge([four, five, one]);
res = print(res);
test.value(res).is([-15,-5,-5,-4,2,3,5,5,15,15]);

var one = new listNode(-8, new listNode(2, new listNode(4)));
var five = new listNode(-9, new listNode(-9, new listNode(-9, new listNode(-9, new listNode(-8, new listNode(-5, new listNode(-3, new listNode(-2, new listNode(1)))))))));
var four = new listNode(-9, new listNode(-7, new listNode(-5, new listNode(-3, new listNode(-3, new listNode(-1, new listNode(0, new listNode(3, new listNode(4)))))))));
var two = new listNode(-9, new listNode(-7, new listNode(-6, new listNode(-4, new listNode(-2, new listNode(-1, new listNode(3, new listNode(4))))))));
var seven = new listNode(-10, new listNode(-3, new listNode(0)));
var six = new listNode(-9, new listNode(0, new listNode(4)));
var eight = new listNode(-8, new listNode(-8));

res = merge([four, five, one, two, seven, six, eight]);
res = print(res);
test.value(res).is([-10,-9,-9,-9,-9,-9,-9,-9,-8,-8,-8,-8,-7,-7,-6,-5,-5,-4,-3,-3,-3,-3,-2,-2,-1,-1,0,0,0,1,2,3,3,4,4,4,4]);

