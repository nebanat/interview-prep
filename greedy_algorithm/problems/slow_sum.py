def get_total_time(arr):
    arr = sorted(arr, reverse=True)
    penalty = 0
    
    while len(arr) > 1:
        sum = (arr[0] + arr[1])
        penalty += sum
        print(penalty)
        arr = arr[2:]
        arr.insert(0, sum)
        print(arr)
        print('#' * 20)
    return penalty

if __name__ == '__main__':
    arr = [4, 2, 1, 3]
    print(get_total_time(arr))