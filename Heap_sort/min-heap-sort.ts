export function minHeapSort(arr) {
    let i = arr.length - 1;
    while (i > 0) {
        let element = arr[i];
        let parentIndex = parseInt(Number((i - 1) / 2).toString());
        let parent = arr[parentIndex];

        if (parent > element) {
            arr[parentIndex] = element;
            arr[i] = parent;

            let leftIndex = i * 2 + 1;
            let rightIndex = i * 2 + 2;
            if (leftIndex < arr.length && arr[i] > arr[leftIndex] || rightIndex < arr.length && arr[i] > arr[rightIndex]) {
                i = rightIndex + 1;
            }
        }

        i--;
    }

    return arr;
}

module.exports = minHeapSort;
