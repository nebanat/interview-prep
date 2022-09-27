def fibonacci(n, memo = {}):
    # time complexity without memoization: O(2^n+m)
    # space complexity without memoization: O(n+m)
    # time complexity with memoization: O(n*m)
    # space complexity wit memoization: O(n+m)
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1
    
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    
    return memo[n]

if __name__ == '__main__':
    print(fibonacci(6))
    print(fibonacci(7))
    print(fibonacci(8))
    print(fibonacci(50))