var test = require('unit.js');
var bfs = require('../Tree/bfs');
var dfs = require('../Tree/dfs');

/******************************************
 * Use the helper code below to implement *
 * and test your function above           *
 ******************************************/

// Constructor to create a new Node
function Node(cost) {
    this.value = cost;
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

root.children.push(five);
root.children.push(three);
root.children.push(six);
five.children.push(four);
three.children.push(two);
two.children.push(one);
three.children.push(zero);
six.children.push(new Node(1));
six.children.push(new Node(5));
zero.children.push(ten);
one.children.push(new Node(1));

var queue = bfs(null);
var list = dfs(null);
test.value(queue).is([]);
test.value(list).is([]);

queue = bfs(root);
list = dfs(root);
test.value(queue).is([0, 5, 3, 6, 4, 2, 0, 1, 5, 1, 10, 1]);
test.value(list).is([0, 5, 4, 3, 2, 1, 1, 0, 10, 6, 1, 5]);
