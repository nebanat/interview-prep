# gcd(a, b) = gcd(b, a-b)
# let assume the first number is greater than the second number

def gcd(a, b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def multiply(n, a):
    """_summary_

    Args:
        n (_type_): _description_
        a (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n == 1:
        return a
    return a + multiply(n - 1, a)

def exponentiation(a, n):
    """_summary_

    Args:
        a (_type_): _description_
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n == 1:
        return a 
    return a * exponentiation(a, n - 1)

def len_string(string):
    """_summary_

    Args:
        string (_type_): _description_

    Returns:
        _type_: _description_
    """
    if string == '':
        return 0
    return 1 + len_string(string[1:])


if __name__ == '__main__':
    input_str = 'I love recursion'
    print(gcd(32, 12))
    print(exponentiation(5, 3))
    print(exponentiation(2, 4))
    print(len_string(input_str))
    # print(multiply(4, 5))
    # print(multiply(5, -4))
    # print(multiply(1, 4))
    # print(multiply(7, 8))