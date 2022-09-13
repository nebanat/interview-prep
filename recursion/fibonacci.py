from re import M


def fibonacci_iterative(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a

def fibonacci_recursive(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_of_digits(array):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(array) == 0:
        return 0
    
    return array[0] + sum_of_digits(array[1:])


if __name__ == '__main__':
    print(sum_of_digits([1, 2, 3, 4, 5]))
    # print(fibonacci_iterative(6))
    # print(fibonacci_recursive(6))