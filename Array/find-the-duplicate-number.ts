// Using floyd' s cycle finder
function findDuplicateNumber(inputArray) {
    let dup = 0;
    // using slow and fast pointer
    let slow = 0;
    let fast = 0;

    // loop until pointers meet
    do {
        slow = inputArray[slow];
        fast = inputArray[inputArray[fast]];
    } while (slow != fast)

    //the first element where they meet is where the cycle starts
    while (dup != slow) {
        dup = inputArray[dup];
        slow = inputArray[slow];
    }

    return dup;
}

module.exports = findDuplicateNumber;
