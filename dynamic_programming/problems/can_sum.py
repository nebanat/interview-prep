def canSum(target, array, memo={}):
    # time complexity without memoization: O(n^^m)
    # time complexity without memoization: O(m)
    # time complexity with memoization: O(n*m)
    # time complexity with memoization: O(m)
    if target in memo:
        return memo[target]
    
    if target == 0: return True
    if target < 0: return False
    
    for num in array:
        remainder = target - num 
        if canSum(remainder, array, memo):
            memo[target] = True
    memo[target] = False
    return memo[target]


#             7
#    2(-5)   4(-3)            3(-4)    0(-7)    
#           1(-3), 0(-4)      0(-3)