## Find a cycle in a linkedlist
- One: Use a second list which stores previously visted nodes.
Resulting in a O(n) space because the second list is essentially storing
n-1 nodes if there is a cycle.

- Two: Use 2 pointers to traverse the linked list. One fast pointer
ahead of a slower pointer. If the two pointer meet then the fast pointer
has encountered a cycle. In a cycle, at most the fast pointer would have visited 2n nodes
and the slow pointer n nodes.

## Deletion in a linked list
1) A linkedlist of size 1
2) deletion of the head
3) deletion of the last element
4) deletion of a middle element

## Finding the mth element
Using two pointers, start the fast pointer m steps ahead of the slow pointer and let the
pointers move one node at a time until the fast pointer reaches the end. the slow pointer
is pointing at the mth element

## Two stacks in one array

## Implement a queue using two stacks

## Implement a stack using two queues 

## Add two numbers
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

## Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the 
two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, 
it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; 
There are 3 nodes before the intersected node in B.

## Merge k Sorted Lists
Given K sorted linked lists of size N each, merge them and print the sorted output.
Merge k sorted linked lists and return it as one sorted list.
