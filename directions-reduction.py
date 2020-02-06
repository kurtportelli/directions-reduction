def dirReduc(arr):
    directions = {'NORTH': 1, 'SOUTH' : -1, 'WEST': 2, 'EAST': -2}
    index = 1
    while index < len(arr):
        if directions[arr[index]] + directions[arr[index-1]] == 0:
            del arr[index]
            del arr[index-1]
            if index > 1: index -= 1
        else: index += 1
    return arr
