import heapq

def k_largest(array, k):
    array = [-elem for elem in array]
    heapq.heapify(array) 

    for i in range(k - 1):
        heapq.heappop(array)
    return -heapq.heappop(array)
    
    # n = len(array)
    # array.sort()
    # return array[n - k]

    # for i in range(k - 1):
    #     array.remove(max(array))
    # return max(array)
