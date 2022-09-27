def howSum(target, numbers, memo={}):
    # time complexity without memoization: O(n^^m * m)
    # time complexity without memoization: O(m)
    # time complexity with memoization: O(n*m^2)
    # time complexity with memoization: O(m^2)
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    for number in numbers:
        remainder = target - number
        remainderResult = howSum(remainder, numbers, memo)

        if remainderResult is not None:
            memo[target] = remainderResult + [ number ]
            return memo[target]

    memo[target] =  None
    return None
