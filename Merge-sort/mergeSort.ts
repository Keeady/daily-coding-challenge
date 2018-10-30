function sortElements(elements: number[]) {
    return mergeSort(elements, 0, elements.length);
}

function mergeSort(elements, p, r) {
    let q;
    if (r - p > 1) {
        q = (p + r) / 2;
        q = parseInt(q.toString());
        mergeSort(elements, p, q);
        mergeSort(elements, q, r);
        merge(elements, p, q, r);
    }
}

function merge(elements, p, q, r) {
    let left = [];
    let right = [];
    let i = p;
    let j = q;
    while (i < q) {
        left.push(elements[i]);
        i++;
    }

    while (j < r) {
        right.push(elements[j]);
        j++;
    }

    i = 0;
    j = 0;
    while (p < r) {
        if (i < left.length && (j >= right.length || left[i] <= right[j])) {
            elements[p] = left[i];
            i++;
        } else {
            elements[p] = right[j];
            j++;
        }

        p++;
    }

    return elements;
}

module.exports = sortElements;
