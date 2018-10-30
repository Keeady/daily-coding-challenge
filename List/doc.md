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
