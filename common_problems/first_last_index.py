def firstLastIndex(array, target):
    # time complexity: O(n)
    # space complexity: O(1)
    indices = []
    left = 0
    right = len(array) - 1

    while left <= right:
        # left index
        if array[left] == target:
            indices.append(left)
        elif array[left] < target:
            left += 1
        
        # right index
        if array[right] == target:
            indices.append(right)
        elif array[right] > target:
            right -= 1
        
        if len(indices) == 2:
            break
    
    return indices if indices else [-1, -1]
    # indices = []
    # for i in len(array):
    #     if array[i] == target:
    #         indices.append(i)
    
    # if indices:
    #     min_index = min(indices)
    #     max_index = max(indices)
    # return [min_index, max_index]
