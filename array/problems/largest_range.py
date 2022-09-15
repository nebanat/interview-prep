# [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 15]

# [15, 12, 11, 10, 7, 6, 5, 4, 3, 2, 1, 0]

# algorithms 
# largest_range = []
# number_range = []



def largest_range(array):
    # O(n) time | O(n) space
    best_range = []
    longest_length = 0
    nums = { num:True for num in array }

    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        current_length = 1
        left = num - 1
        right = num + 1 

        while left in nums:
            nums[left] = False
            current_length += 1
            left -= 1
        
        while right in nums:
            nums[right] = False
            current_length += 1
            right += 1
        
        if current_length > longest_length:
            longest_length = current_length
            best_range = [left + 1, right - 1]
    
    return best_range

if __name__ == '__main__':
    l = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    print(largest_range(l))