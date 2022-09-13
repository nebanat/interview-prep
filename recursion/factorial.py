def factorial_iterative(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    prod = 1
    
    if n <= 1:
        return prod

    for i in range(1, n + 1):
        prod = prod * i
    
    return prod


def factorial_recursive(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    # base case
    if n <= 1:
        return 1
    # move towards the base case with n-1 and recursive call
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    print(factorial_iterative(5))
    print(factorial_recursive(5))
    print(factorial_recursive(-10))
    # print("hello world")
    