- Check if a string containing a group of nested parentheses are 
correct or not:
    - Using a stack, if it's an opening bracket, push into the stack
    - If it's a closing bracket, pop the stack:
        - true if opening bracket is popped
        - false otherwise
- Given a string containing parentheses:
    - Find the list or count the number of parentheses that are incorrect
    - Same as above, instead of stopping when a closing bracket
    is found, increment count and continue popping until an opening
    bracket is found. Every closing bracket found increments the counter 
    
 ##### Considerations:
 - Does the string contains other characters like alphanumerics,
 spaces and punctuations, besides the parentheses and brackets.
    - Create a whitelist of parentheses and brackets so that
    it's easy to ignore/skip all the rest
    -  Create a blacklist if the set is small enough

## Find sets of words
- Given an input list of words and a string, output every different set of words that you can find in the string from the given words. For example,
input: word_list = ['dog', 'cats', 'sand', 'cat', 'and'], string = "catsanddog"
output: [ ['cat', 'sand', 'dog'], ['cats', 'and', 'dog'] ]  

## Ransom Note
You are given a magazine and a ransom note. Write an algorithm to determine if the magazine contains sufficient 
characters to cut out and construct the ransom note.  

## Seating arrangement
Given a string representing taken seats on a plane and a number N representing the rows 
on a plane, return the amount of seating arrangements for a family of 3. 
Seating between isles is not a possible arrangement. The seating columns are as follows: ABC | DEFG| HJK

## First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

## Reverse a string
Write a function that takes a string as input and returns the string reversed.

## Reverse a String ||
Given a string and an integer k, you need to reverse the first k characters for every 2k characters
 counting from the start of the string. If there are less than k characters left, reverse all of 
 them. If there are less than 2k but greater than or equal to k characters, then reverse the first
  k characters and left the other as original.
  
## Longest palindrome substring
Given a string s, find the longest palindromic substring in s. You may assume that 
the maximum length of s is 1000.
   
## String to Integer (atoi)


## Folder path tree structure
Given a list of strings containing folder paths, convert it into a tree structure, using a language of your choice.  