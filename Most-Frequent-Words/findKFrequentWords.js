// [the, brown, fox, likes, the, brown, meat, fox, likes, pie, too]
//k=4
//fh=[1, 1, 1, 2]
//wf=[the->2, brown->1, fox->1, likes->1]
//m=[0->brown, 1->fox, 2->likes, 3->the]
function findKFrequentWords(textBody, k) {
    var i = 0;
    //split words
    var words = textBody.split(' ');
    //k length heap
    var frequencyHeap = [];
    //build hashtable of k length
    var mostFrequentTable = new Map();
    while (i < k) {
        mostFrequentTable.set(i, null);
        i++;
    }
    //hash table of all words frequency
    var wordFrequency = new Map();
    // iterate over array of words
    for (i = 0; i < words.length; i++) {
        var freq = 0;
        if (wordFrequency.has(words[i])) {
            freq = wordFrequency.get(words[i]);
        }
        freq += 1;
        //update word's frequency count
        wordFrequency.set(words[i], freq);
        // insertion in heap
        // case heap is empty
        // case heap is not full
        // case heap is full
        if (frequencyHeap.length === 0 || frequencyHeap.length < k || frequencyHeap.length === k && freq > frequencyHeap[0]) {
            //case full: remove the smallest frequency
            if (frequencyHeap.length === k) {
                minHeapRemove(frequencyHeap, mostFrequentTable);
            }
            mostFrequentTable = minHeapInsert(frequencyHeap, freq, mostFrequentTable, words[i]);
        }
    }
    // a k length min heap to store the frequency of the k most frequent words
    // if any frequency larger than min
    // min is thrown out and new frequency is added to the heap
    // if heap has empty cells, add new frequency
    // a hashtable with keys 0 to k-1 points to the position in heap
    // value at each position is the frequent word
    // when heap change, using previous index and new index, move words around
    // in the hashtable
    var kFrequentWords = {};
    for (i = 0; i < k; i++) {
        var word = mostFrequentTable.get(i);
        kFrequentWords[word] = wordFrequency.get(word);
    }
    return kFrequentWords;
}
function minHeapInsert(arr, value, mostFrequentTable, word) {
    arr.push(value);
    if (arr.length === 1) {
        mostFrequentTable.set(0, word);
        return mostFrequentTable;
    }
    var i = arr.length - 1;
    mostFrequentTable.set(i, word);
    while (i > 0) {
        var parentIndex = parseInt(Number((i - 1) / 2).toString());
        var parent_1 = arr[parentIndex];
        if (parent_1 > value) {
            // move parentIndex position from hash table to i position
            var parentNode = mostFrequentTable.get(parentIndex);
            // move i position to parentIndex position
            var childNode = mostFrequentTable.get(i);
            arr[parentIndex] = value;
            arr[i] = parent_1;
            mostFrequentTable.set(parentIndex, childNode);
            mostFrequentTable.set(i, parentNode);
            i = parentIndex;
        }
        else {
            return mostFrequentTable;
        }
    }
    return mostFrequentTable;
}
function minHeapRemove(arr, mostFrequentTable) {
    arr.shift();
    var i = 0;
    while (i < arr.length) {
        var parent_2 = arr[i];
        var leftIndex = i * 2 + 1;
        var rightIndex = i * 2 + 2;
        if (leftIndex >= arr.length) {
            return mostFrequentTable;
        }
        if (arr[leftIndex] < arr[i]) {
            // move parentIndex position from hash table to i position
            var parentNode = mostFrequentTable.get(i);
            // move i position to parentIndex position
            var childNode = mostFrequentTable.get(leftIndex);
            arr[i] = arr[leftIndex];
            arr[leftIndex] = parent_2;
            mostFrequentTable.set(i, childNode);
            mostFrequentTable.set(leftIndex, parentNode);
        }
        if (rightIndex < arr.length && arr[rightIndex] < arr[i]) {
            arr[i] = arr[rightIndex];
            arr[rightIndex] = arr[i];
        }
        i++;
    }
    return mostFrequentTable;
}
module.exports = findKFrequentWords;
