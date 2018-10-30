var treeNode = require("../Tree/TreeNode");

var test = require('unit.js');
var binaryTreeHeight = require('../Tree/binaryTreeHeight');

var result = binaryTreeHeight(null);
test.value(result).is(0);

var root = new treeNode.TreeNode(1);
result = binaryTreeHeight(root);
test.value(result).is(1);

var two = new treeNode.TreeNode(2);
root.setLeft(two);
var three = new treeNode.TreeNode(3);
root.setRight(three);
var four = new treeNode.TreeNode(4);
two.setLeft(four);

result = binaryTreeHeight(root);
test.value(result).is(3);

var five = new treeNode.TreeNode(5);
two.setRight(five);
var six = new treeNode.TreeNode(6);
three.setLeft(six);
var seven = new treeNode.TreeNode(7);
six.setRight(seven);
result = binaryTreeHeight(root);
test.value(result).is(4);
