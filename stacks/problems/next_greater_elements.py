# array = [2, 5, -3, -4, 6, 7, 2]
# [5, 6, 6, 6, 7, -1, 5 ]

# array = [0, 1, 2, 3, 4]
# [1,2, 3, 4, -1 ]

# index 0, n_greatest = []

# solutionOne

def nextGreaterElement(array):
    # left to right 
    result = [-1] * len(array)
    stack = []

# solutionOne
def nextGreaterElementTwo(array):
    # right to left 
    result = [-1 for _ in range(len(array))]
    stack = []

    for idx in range(2 * len(array) - 1, -1, -1):
        circular_idx = idx % len(array)

        while len(stack) > 0:
            if stack[len(stack) - 1] <= array(circular_idx):
                stack.pop()
            else:
                result[circular_idx] = stack[len(stack) - 1]
                break 

            stack.append(array[circular_idx])
    return result