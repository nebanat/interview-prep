# a = [5, 1, 4, 2] 


# Iter 1 
# current_num = 5, a = [1, 4, 2], product_list = [8]

# Iter 2 
# current_num = 1, a = [5, 4, 2], product_list = [8, 40]

# Iter 3 
# current_num = 4, a = [5, 1, 2], product_list = [8, 40, 10]

# Iter 4
# current_num = 2, a = [5, 1, 4], product_list = [8, 40, 10, 20]

def arrayOfProducts(array):
    # time complexity: O(n ^ 2), space complexity: O(n)
    product_list = []
    for i in range(len(array)):
        product_num = 1
        for j in range(len(array)):
            if j != i:
                product_num *= array[j]
        product_list.append(product_num)
    return product_list

if __name__ == '__main__':
    print(arrayOfProducts([5,1,4,2]))


# more efficient solution
# a = [5, 1, 4, 2] , left_array = [1, 1, 1, 1], right_array = [1, 1, 1, 1]

def arrayofProductsEfficient(array):
    left_array = [1 for _ in range(len(array))]
    right_array = [1 for _ in range(len(array))]
    products = [1 for _ in range(len(array))]

    left_product = 1
    for i in range(len(array)):
        left_array[i] = left_product
        left_product *= array[i]
    
    right_product = 1
    for i in reversed(range(len(array))):
        right_array[i] = right_product
        right_product *= array[i]
    
    for i in range(len(array)):
        products[i] = left_array[i]  * right_array[i]
    
def arrayofProductsMoreEfficient(array):
    products = [1 for _ in range(len(array))]

    left_product = 1
    for i in range(len(array)):
        products[i] = left_product
        left_product *= array[i]
    
    right_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_product
        right_product *= array[i]
    
    return products

# right array
# index 0
# product = 1 * 5, right_array = [1, 1, 1, 1],

# index 1
# product = 5 * 1, right_array = [1, 5, 1, 1],

# index 2
# product = 5 * 4, right_array = [1, 5, 5, 1],

# index 3
# product = 5 * 4, right_array = [1, 5, 5, 20],

# left array a = [5, 1, 4, 2]

#  index 3
# product = 1, left_array = [1, 1, 1, 1]

# index 2
# product = 1 * 2, left_array = [1, 1, 2, 1]

# index 1
# product = 2 * 4, left_array = [1, 8, 2, 1]

# index 0
# product = 8 * 1, left_array = [8, 8, 2, 1]

# left_array = [8, 8, 2, 1], right_array = [1, 5, 5, 20] = [8, 40, 10, 20]