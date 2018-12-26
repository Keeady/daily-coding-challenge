var test = require('unit.js');
var postOrder = require('../Tree/postOrder');
var treeNode = require("../Tree/TreeNode");

var result = postOrder(null);
test.value(result).isUndefined();

var root = new treeNode.TreeNode(50);
result = postOrder(root);
test.value(result).is([50]);

var two = new treeNode.TreeNode(25);
root.setLeft(two);
var three = new treeNode.TreeNode(90);
root.setRight(three);
var four = new treeNode.TreeNode(14);
two.setLeft(four);
var five = new treeNode.TreeNode(30);
two.setRight(five);
var six = new treeNode.TreeNode(75);
three.setLeft(six);
var seven = new treeNode.TreeNode(84);
six.setRight(seven);

result = postOrder(root);
test.value(result).is([84, 75, 90, 30, 14, 25, 50]);
