# Power set
# P ([1, 2, 3])
# = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
# if len(array) == 0: return [[]]
# space and time complexity: O(2^n * n) 

# algorithm walkthrough
# [1, 2, 3]
# subsets: [[]]

# item = 1
    # currentsubset = [1]
    # subsets = [[], [1]]

# item = 2 
    # currentsubset_1 = [] .2 = [2]
    # currentsubset_2 = [1] .2 = [1, 2]
    # subsets= [[], [1], [2], [1, 2]]

# item = 3
    # currentsubset_1 = [] . 3 = [3]
    # currentsubset_2  = [1] .3 = [1, 3]
    # currentsubset_3 = [2] . 3 = [2, 3]
    # currentsubset_4 = [1,2] . 3 = [1,2,3]
    
    # subsets = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def powerset_iterative(array):
    """
    O(2^n * n) time | O(2^n * n) space
    """
    subsets = [[]]

    if not array:
        return subsets
    
    for item in array:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [item])
    return subsets


def powerset_recursive(array, idx=None):
    """Do not fully understand the recursive method"""
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset_recursive(array, idx - 1)

    for i in range(len(subsets)):
        current_subset = subsets[i]
        subsets.append(current_subset + [ele])
    return subsets
