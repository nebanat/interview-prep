def threeNumberSum(array, targetSum):
    # Write your code here.
	# time complexity = O(N^2)
	# space complexity = O(N)
    array = sorted(array)
    target_array = []
    current_sum = 0
    
    for i in range(len(array)- 2):
        left = i + 1
        right = len(array)-1
        
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                target_array.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
                
            elif current_sum < targetSum:
                left += 1
            elif current_sum > targetSum:
                right -= 1
    return target_array
