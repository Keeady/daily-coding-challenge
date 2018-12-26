class ListNode {
    public val;
    public next;
    constructor(val, next: ListNode = null) {
        this.val = val;
        this.next = next;
    }
}

function mergeKSortedList(inputArray: Array<ListNode>) {
    let k = inputArray.length;
    let pointerArray = [];
    let i = 0;
    let head = null;
    let temp;
    let prev;
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
        } else {
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
function addPointer(pointerArray: Array<ListNode>, pointer) {
    if (!pointer) {
        return pointerArray;
    }

    pointerArray.push(pointer);

    if (pointerArray.length === 1) {
        return pointerArray;
    }

    let i = pointerArray.length - 1;
    let parentIndex;
    while (i > 0) {
        parentIndex = parseInt(Number((i - 1) / 2).toString());
        let parent = pointerArray[parentIndex];
        let child = pointerArray[i];
        if (parent.val > child.val) {
            pointerArray[parentIndex] = child;
            pointerArray[i] = parent;
            i = parentIndex;
        } else {
            return pointerArray;
        }
    }

    return pointerArray;
}

function removePointer(pointerArray: Array<ListNode>) {
    let min = pointerArray[0];
    if (pointerArray.length === 1) {
        pointerArray.pop();
        return min;
    }

    pointerArray[0] = /*min.next ? min.next : */ pointerArray.pop();

    let i = 0;
    while (i < pointerArray.length) {
        let parent = pointerArray[i];
        let leftChildIndex = 2 * i + 1;
        let rightChildIndex = 2 * i + 2;
        let childIndex;

        if (rightChildIndex < pointerArray.length) {
            childIndex = pointerArray[leftChildIndex].val <= pointerArray[rightChildIndex].val ? leftChildIndex : rightChildIndex;
        } else if (leftChildIndex < pointerArray.length) {
            childIndex = leftChildIndex;
        } else {
            return min;
        }

        if (parent.val > pointerArray[childIndex].val) {
            pointerArray[i] = pointerArray[childIndex];
            pointerArray[childIndex] = parent;
        } else {
            return min;
        }

        i++;
    }

    return min;
}
module.exports = {mergeKSortedList, ListNode};
