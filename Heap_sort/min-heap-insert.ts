export function minHeapInsert(arr, value) {
    arr.push(value);

    if (arr.length === 1) {
        return arr;
    }

    let i = arr.length - 1;
    while (i > 0) {
        let parentIndex = parseInt(Number((i - 1) / 2).toString());
        let parent = arr[parentIndex];
        if (parent > value) {
            arr[parentIndex] = value;
            arr[i] = parent;
            i = parentIndex;
        } else {
            return i;
        }
    }

    return i;
}

module.exports = minHeapInsert;
