# Quick sort algorithm
# Quick sort is a divide and conquer algorithm, 
# which means that it divides the array into two parts and 
# then recursively calls itself on the two parts.

def quick_sort(array):
    """_summary_

    Args:
        array (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    print(quick_sort([3, 6, 8, 10, 1, 2, 1]))