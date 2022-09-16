# array = [3, 5, -4, 8, 11, 1, -1, 6] target = 10 

# result : {}
# iter 1: 10 - 3 = 8, result: {3:8}
# iter 2: 10 - 5 = 5, result: {3:8, 5:5}
# iter 3: 10 + 4  = 14, result: {3:8, 5:5, -4:14}
# iter 4: 10 - 8 = 2, result: {3:8, 5:5, -4:14, 8:2, }
# iter 5: 10 - 11 = -1, result: {3:8, 5:5, -4:14, 8:2, 11: -1 }
# iter 6: 10 - 1 = 9, result: {3:8, 5:5, -4:14, 8:2, 11: -1, 1:9,  }
# iter 7: 10 + 1 = 11, result: {3:8, 5:5, -4:14, 8:2, 11: -1, 1:9,  }

def two_number_sum(array, target):
    if not array:
        return []
    
    result = {}
    for num in array:
        other_num = target - num
        
        if other_num in result:
            return [other_num, num]
        else:
            result[num] = other_num
    return []

if __name__ == '__main__':
    print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))