var test = require('unit.js');
var getCheapestCost = require('../Tree/getCheapestCost');

/******************************************
 * Use the helper code below to implement *
 * and test your function above           *
 ******************************************/

// Constructor to create a new Node
function Node(cost) {
    this.cost = cost;
    this.children = [];
}

let root = new Node(0);
let five = new Node(5);
let three = new Node(3);
let six = new Node(6);
let two = new Node(2);
let zero = new Node(0);
let one = new Node(1);
let four = new Node(4);
let ten = new Node(10);

var val = getCheapestCost(root);
test.value(val).is(0);

root.children.push(five);
root.children.push(three);
root.children.push(six);

val = getCheapestCost(root);
test.value(val).is(3);

five.children.push(four);
three.children.push(two);
two.children.push(one);
three.children.push(zero);

val = getCheapestCost(root);
test.value(val).is(3);

six.children.push(new Node(1));
six.children.push(new Node(5));
zero.children.push(ten);
one.children.push(new Node(1));

val = getCheapestCost(root);
test.value(val).is(7);
