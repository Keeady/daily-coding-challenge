from math import sqrt

# todo skip dictionary, use object

def find_k_closest_points(points, k):
    if k == 0:
        return []

    heap = []
    k_distance_dict = {}

    for i in range(0, len(points)):
        distance = calc_distance(points[i])
        max = find_max_index_in_heap(heap)
        if len(heap) < k or distance < heap[max]:
            heap = max_heap_add(k, heap, k_distance_dict, distance, points[i])

    return list(k_distance_dict.values())


def find_max_index_in_heap(heap):
    if len(heap) == 0:
        return 0
    index = len(heap) // 2
    maximumElement = heap[index]

    for i in range(1 + len(heap) // 2, len(heap)):
        if maximumElement < heap[i]:
            maximumElement = heap[i]
            index = i

    return index

def calc_distance(point):
    return point[0]**2 + point[1]**2


def max_heap_add(k, heap, k_distance_dict, distance, point):
    if len(heap) == k:
        max_index = find_max_index_in_heap(heap)
        heap[max_index] = distance
        k_distance_dict[max_index] = point
        #max_heap_remove(k, heap, k_distance_dict)
    else:
        heap.append(distance)
        k_distance_dict[len(heap) - 1] = point

    if len(heap) == 1:
        return heap

    return balance_heap(heap, k_distance_dict)


def max_heap_remove(k, heap, k_distance_dict):

    last_distance = heap.pop()
    k_distance_dict[0] = k_distance_dict[k - 1]
    k_distance_dict[k - 1] = None

    if len(heap) == 0:
        return heap

    heap[0] = last_distance

    i = 0
    while i < len(heap):
        parent = heap[i]
        left_child = i * 2 + 1
        right_child = i * 2 + 2
        child_index = left_child

        if right_child < len(heap):
            if heap[right_child] < heap[left_child]:
                child_index = right_child
        elif left_child < len(heap):
            child_index = left_child
        else:
            return heap

        if parent > heap[child_index]:
            heap[i] = heap[child_index]
            heap[child_index] = parent

            prev_parent_point = k_distance_dict[i]
            k_distance_dict[i] = k_distance_dict[child_index]
            k_distance_dict[child_index] = prev_parent_point
        else:
            return heap

        i += 1

    return heap


def balance_heap(heap, k_distance_dict):
    index = len(heap) - 1

    while index > 0:
        parent_index = int((index - 1) / 2)
        if heap[parent_index] > heap[index]:
            parent = heap[parent_index]
            heap[parent_index] = heap[index]
            heap[index] = parent

            prev_parent_point = k_distance_dict[parent_index]
            k_distance_dict[parent_index] = k_distance_dict[index]
            k_distance_dict[index] = prev_parent_point

            index = parent_index

        else:
            return heap

    return heap



#[[-173, 399], [62, -213], [71, 282], [-45, 851], [710, 982], [493, 985], [-529, -946], [-83, 78], [624, -785], [877, -351], [500, -376], [-601, -305], [-23, -79], [-82, 906], [-143, 500], [-249, -260], [10, 706], [-904, -632], [-402, 458], [303, -970], [93, -552], [-362, -743], [705, 986], [900, -524], [-680, -204], [-726, 890], [-138, 742], [-76, 714], [813, 474], [443, 23], [-422, 117], [768, 214], [863, 562], [728, -204], [778, 147], [-56, -751], [240, 454], [-106, -701], [-897, -770], [572, 433], [-658, 97], [-301, -466], [902, -371], [-38, -662], [-872, 191], [659, 294], [852, 965], [-37, 665], [541, -920], [-537, 704]]
#{0: 189130, 1: 49213, 2: 84565, 3: 726226, 4: 1468424, 5: 1213274, 6: 1174757, 7: 12973, 8: 1005601, 9: 892330, 10: 391376, 11: 454226, 12: 6770, 13: 827560, 14: 270449, 15: 129601, 16: 498536, 17: 1216640, 18: 371368, 19: 1032709, 20: 313353, 21: 683093, 22: 1469221, 23: 1084576, 24: 504016, 25: 1319176, 26: 569608, 27: 515572, 28: 885645, 29: 196778, 30: 191773, 31: 635620, 32: 1060613, 33: 571600, 34: 626893, 35: 567137, 36: 263716, 37: 502637, 38: 1397509, 39: 514673, 40: 442373, 41: 307757, 42: 951245, 43: 439688, 44: 796865, 45: 520717, 46: 1657129, 47: 443594, 48: 1139081, 49: 783985}
#[1657129, 1469221, 1319176, 1397509, 1468424, 1213274, 1174757, 1005601, 1060613, 951245, 1216640, 1139081, 1084576, 885645, 270449, 635620, 626893, 567137, 726226, 514673, 892330, 796865, 1032709, 504016, 783985, 6770, 569608, 515572, 827560, 196778, 191773, 12973, 498536, 129601, 571600, 49213, 263716, 371368, 502637, 189130, 442373, 307757, 313353, 391376, 439688, 520717, 683093, 84565, 443594, 454226]
#{0: [852, 965], 1: [705, 986], 2: [-726, 890], 3: [-897, -770], 4: [710, 982], 5: [493, 985], 6: [-529, -946], 7: [624, -785], 8: [863, 562], 9: [902, -371], 10: [-904, -632], 11: [541, -920], 12: [900, -524], 13: [813, 474], 14: [-143, 500], 15: [768, 214], 16: [778, 147], 17: [-56, -751], 18: [-45, 851], 19: [572, 433], 20: [877, -351], 21: [-872, 191], 22: [303, -970], 23: [-680, -204], 24: [-537, 704], 25: [-23, -79], 26: [-138, 742], 27: [-76, 714], 28: [-82, 906], 29: [443, 23], 30: [-422, 117], 31: [-83, 78], 32: [10, 706], 33: [-249, -260], 34: [728, -204], 35: [62, -213], 36: [240, 454], 37: [-402, 458], 38: [-106, -701], 39: [-173, 399], 40: [-658, 97], 41: [-301, -466], 42: [93, -552], 43: [500, -376], 44: [-38, -662], 45: [659, 294], 46: [-362, -743], 47: [71, 282], 48: [-37, 665], 49: [-601, -305]}