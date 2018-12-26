//https://leetcode.com/problems/evaluate-reverse-polish-notation/
function reversePolishNotation(inputArray) {
    var index;
    var operandStack = [];
    var leftOperand;
    var rightOperand;
    var value;
    //iterate the input array
    // if current element is a operand, push into the stack
    // if operator, pop 2 elements from stack then push result in stack
    for (index = 0; index < inputArray.length; index++) {
        if (inputArray[index] == '+' || inputArray[index] == '-' || inputArray[index] == '*' ||
            inputArray[index] == '/') {
            rightOperand = operandStack.pop();
            leftOperand = operandStack.pop();
            value = evaluateSequence(inputArray[index], leftOperand, rightOperand);
            operandStack.push(parseInt(value));
        }
        else {
            operandStack.push(parseInt(inputArray[index]));
        }
    }
    return operandStack.pop();
}
function evaluateSequence(operator, leftOperand, rightOperand) {
    var value;
    switch (operator) {
        case '*':
            value = multiply(leftOperand, rightOperand);
            break;
        case '-':
            value = subtract(leftOperand, rightOperand);
            break;
        case '+':
            value = add(leftOperand, rightOperand);
            break;
        case '/':
            value = divide(leftOperand, rightOperand);
            break;
        default:
            throw 'Invalid operator';
    }
    return value;
}
function add(leftOperand, rightOperand) {
    return leftOperand + rightOperand;
}
function multiply(leftOperand, rightOperand) {
    return leftOperand * rightOperand;
}
function subtract(leftOperand, rightOperand) {
    return leftOperand - rightOperand;
}
function divide(leftOperand, rightOperand) {
    return leftOperand / rightOperand;
}
module.exports = reversePolishNotation;
