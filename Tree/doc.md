## Preorder without recursion
By understanding how the recursion works using stacks
Implement the preorder using a stack to store nodes which will be printed at a later time
- Pop the stack
- Print the popped node
- Add the right child in stack
- Add the left child in stack
- Loop continues until stack is empty


## Lowest common ancestor


## Validate BST
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

## Binary Tree Symmetric


## Closest binary search tree value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

## Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

## Maximum Binary Tree
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

