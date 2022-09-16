import random

# array = [13, 29, 39, 47, 54, 57, 63, 67, 82, 83]
# target = 82 
# target 39 

# target 82
# iter 1:left = 0, right = 9, mid = 9//2=4, array[mid]=54
# iter 2:left = 5, right = 9, mid = 9 + 5//2=7, array[mid]=67
# iter 3: left = 8, right =9, mid 9 + 8//2=8, array[mid]=82

# target 39
# iter 1:left = 0, right = 9, mid = 9//2=4, array[mid]=54
# iter 2:left = 0, right = 3, mid = 3+0//2=1, array[mid]=29
# iter 3: left = 2, right =3, mid 3 + 2//2=2, array[mid]=39

# target 100
# iter 1:left = 0, right = 9, mid = 9//2=4, array[mid]=54
# iter 2:left = 5, right = 9, mid = 9 + 5//2=7, array[mid]=67
# iter 3: left = 8, right =9, mid 9 + 8//2=8, array[mid]=82
# iter 4: left=9, right =9



def binary_search(data, target):
    if not data:
        return -1
    
    left = 0
    right = len(data)  - 1

    while left <= right:
        mid = (left + right) // 2
        
        if target == data[mid]:
            return mid
        elif target > data[mid]:
            left = mid + 1
        elif target < data[mid]:
            right = mid - 1
    
    return - 1


if __name__ == '__main__':
    n = 10
    max_val  = 100
    data = [random.randint(1, max_val) for i in range(n)]
    data.sort()
    print(data)