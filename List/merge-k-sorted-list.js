var ListNode = /** @class */ (function () {
    function ListNode(val, next) {
        if (next === void 0) { next = null; }
        this.val = val;
        this.next = next;
    }
    return ListNode;
}());
function mergeKSortedList(inputArray) {
    var k = inputArray.length;
    var pointerArray = [];
    var i = 0;
    var head = null;
    var temp;
    var prev;
    if (k == 0) {
        return head;
    }
    while (i < k) {
        addPointer(pointerArray, inputArray[i]);
        i++;
    }
    while (pointerArray.length != 0) {
        temp = removePointer(pointerArray);
        if (!head) {
            head = temp;
        }
        else {
            prev.next = temp;
        }
        prev = temp;
        addPointer(pointerArray, temp.next);
    }
    return head;
}
/**
 * min heap to keep pointers sorted
 * @param pointerArray
 * @param pointer
 */
function addPointer(pointerArray, pointer) {
    if (!pointer) {
        return pointerArray;
    }
    pointerArray.push(pointer);
    if (pointerArray.length === 1) {
        return pointerArray;
    }
    var i = pointerArray.length - 1;
    var parentIndex;
    while (i > 0) {
        parentIndex = parseInt(Number((i - 1) / 2).toString());
        var parent_1 = pointerArray[parentIndex];
        var child = pointerArray[i];
        if (parent_1.val > child.val) {
            pointerArray[parentIndex] = child;
            pointerArray[i] = parent_1;
            i = parentIndex;
        }
        else {
            return pointerArray;
        }
    }
    return pointerArray;
}
function removePointer(pointerArray) {
    var min = pointerArray[0];
    if (pointerArray.length === 1) {
        pointerArray.pop();
        return min;
    }
    pointerArray[0] = /*min.next ? min.next : */ pointerArray.pop();
    var i = 0;
    while (i < pointerArray.length) {
        var parent_2 = pointerArray[i];
        var leftChildIndex = 2 * i + 1;
        var rightChildIndex = 2 * i + 2;
        var childIndex = void 0;
        if (rightChildIndex < pointerArray.length) {
            childIndex = pointerArray[leftChildIndex].val <= pointerArray[rightChildIndex].val ? leftChildIndex : rightChildIndex;
        }
        else if (leftChildIndex < pointerArray.length) {
            childIndex = leftChildIndex;
        }
        else {
            return min;
        }
        if (parent_2.val > pointerArray[childIndex].val) {
            pointerArray[i] = pointerArray[childIndex];
            pointerArray[childIndex] = parent_2;
        }
        else {
            return min;
        }
        i++;
    }
    return min;
}
module.exports = { mergeKSortedList: mergeKSortedList, ListNode: ListNode };
