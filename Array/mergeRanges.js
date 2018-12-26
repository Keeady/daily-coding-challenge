function mergeRanges(ranges) {
    var mergedRanges = [];
    if (ranges.length === 0 || ranges.length === 1) {
        return ranges;
    }
    //sort by starting time
    ranges.sort(function (item1, item2) {
        return item1[0] > item2[0];
    });
    //iterate through each range items
    // if mergedRange is empty
    // push range
    // set prev range to last element in mergedRange
    // if low and high are within the prev range
    // skip
    // if low is outside and high is within
    // change to new low
    // if high is outside and low is within
    // change to new high
    // if low and high outside of prev range
    // push range
    ranges.forEach(function (items) {
        if (mergedRanges.length === 0) {
            mergedRanges.push(items);
            return;
        }
        var prevRange = mergedRanges[mergedRanges.length - 1];
        if (items[0] >= prevRange[0] && items[0] < prevRange[1] && items[1] <= prevRange[1] &&
            items[1] > prevRange[0]) {
            return;
        }
        if (items[0] < prevRange[0] && items[1] <= prevRange[1] && items[1] >= prevRange[0]) {
            mergedRanges[mergedRanges.length - 1] = [items[0], prevRange[1]];
            return;
        }
        if (items[1] > prevRange[1] && items[0] >= prevRange[0] && items[0] <= prevRange[1]) {
            mergedRanges[mergedRanges.length - 1] = [prevRange[0], items[1]];
            return;
        }
        if (items[0] < prevRange[0] && items[1] < prevRange[1] ||
            items[0] > prevRange[0] && items[1] > prevRange[1]) {
            mergedRanges.push(items);
        }
    });
    return mergedRanges;
}
module.exports = mergeRanges;
