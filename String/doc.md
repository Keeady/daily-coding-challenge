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
