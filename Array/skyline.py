def calc_skyline(arr):
    output = []
    prev_building = arr[0]
    output.append([prev_building[0], prev_building[2]])

    for i in range(1, len(arr)):
        building = arr[i]
        left = building[0]
        right = building[1]
        height = building[2]



        # no overlap
        if left > prev_building[1]:
            output.append([prev_building[1], 0])

        prev_countour = output[len(output) - 1]

        if height < prev_countour[1]:
            output.append([prev_building[1], height])

        elif height > prev_countour[1]:
            output.append([left, height])

        prev_building = arr[i]

    output.append([prev_building[1], 0])

    return output

class Building:
    def __init__(self, left, right, height):
        self.left = left
        self.right = right
        self.height = height

def skyline_divide_conquer(arr):
    pass

def merge(buildingA: Building, buildingB: Building):
    output = []

    # start on the same index
    if buildingA.left == buildingB.right:
        # same height, ignore
        max_height = max(buildingA.height, buildingB.height)
        buildingA.height = max_height
        buildingB.height = max_height

        output.append([buildingA.left, max_height])

    else:
        output.append([buildingA.left, buildingA.height])

        if buildingA.height > buildingB.height:
            buildingB.left = buildingA.right
            output.append([buildingB.left, buildingB.height])
