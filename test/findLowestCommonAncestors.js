var test = require('unit.js');
var lowestCommonAncestors = require('../Tree/lowestCommonAncestors');
var treeNode = require("../Tree/TreeNode");

var four = new treeNode.TreeNode(14);
var six = new treeNode.TreeNode(75);

var result = lowestCommonAncestors(null, four, six);
test.value(result).is(null);

var root = new treeNode.TreeNode(50);
result = lowestCommonAncestors(root, four, six);
test.value(result).is(null);

var two = new treeNode.TreeNode(25);
root.setLeft(two);
var three = new treeNode.TreeNode(90);
root.setRight(three);
two.setLeft(four);
var five = new treeNode.TreeNode(30);
two.setRight(five);
three.setLeft(six);
var seven = new treeNode.TreeNode(84);
six.setRight(seven);

result = lowestCommonAncestors(root, four, six);
test.value(result.printValue()).is(root.printValue());

result = lowestCommonAncestors(root, five, seven);
test.value(result.printValue()).is(root.printValue());

result = lowestCommonAncestors(root, four, five);
test.value(result.printValue()).is(two.printValue());
