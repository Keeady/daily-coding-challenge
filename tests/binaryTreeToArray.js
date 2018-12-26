var test = require('unit.js');
var bta = require('../Tree/binaryTreeToArray');
var TreeNode = require('../Tree/TreeNode');
var bottom = new TreeNode.TreeNode(4);
var left = new TreeNode.TreeNode(2, bottom);
var right = new TreeNode.TreeNode(3);
var node = new TreeNode.TreeNode(1, left, right);

var res = bta(node);
test.value(res).is([1, 2, 4, 3]);
