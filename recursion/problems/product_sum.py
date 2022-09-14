# array = [5, 2, [7, -1], 3 [6, [-13, 8], 4]]
# [x, y]

# sum: 0 
# level: 1

# productsum (array, sum)
# if len(array) == 0: return sum
#  for i in range(len(array)):
#   if not instance(item, list): 
#       sum += array.pop()  
#   else: 
#      sum = productsum(array, sum)
# return sum 
# 2 (7 + 1) = 2 * 7 + 2 * 1
# [5, 2, [3, 2], 1]

def product_sum(array, level=1):
    """_summary_

    Args:
        array (_type_): _description_
        level (int, optional): _description_. Defaults to 1.

    Returns:
        _type_: _description_
    """
    sum = 0
    for element in array:
        if isinstance(element, list):
            sum += product_sum(element, level + 1)
        else: 
            sum += element
    return sum * level
    


if __name__ == '__main__':
    print(product_sum([1, 2, [3, 4], 5]))
    