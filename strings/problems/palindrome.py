# abcdcba

# left = 0 
# right = 6
# while left < right:

# iter 1 
# str[0] == str[6]

# iter 2 
# left = 1
# right = 5
# str[1] == str[5]

# iter 3 
# left = 2
# right = 4
# str[2] == str[4]

# iter 4 
# left = 3
# right = 3
def is_palindrome(string):
    # time complexity: O(n)
    # space complexity; O(1)
    left = 0
    right = len(string)  - 1

    while left < right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1
    return True 


if __name__ == '__main__':
    print(is_palindrome("abcdcba"))