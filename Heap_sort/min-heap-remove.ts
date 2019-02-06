export function minHeapRemove(arr) {
    arr[0] = arr.pop();
    let i = 0;
    while (i < arr.length) {
        let parent = arr[i];
        let leftIndex = i * 2 + 1;
        let rightIndex = i * 2 + 2;
        let childIndex;

        if (rightIndex < arr.length) {
            //has 2 children
            if (arr[leftIndex] <= arr[rightIndex]) {
                childIndex = leftIndex;
            } else {
                childIndex = rightIndex;
            }
        } else if (leftIndex < arr.length) {
            childIndex = leftIndex;
        } else {
            // no children
            return arr;
        }

        if (parent > arr[childIndex]) {
            //swap parent and child
            arr[i] = arr[childIndex];
            arr[childIndex] = parent;
        } else {
            return arr;
        }

        i++;
    }

    return arr;
}

module.exports = minHeapRemove;
