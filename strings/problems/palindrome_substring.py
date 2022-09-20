# string = "abaxyzzyxf"
# is_palindrome(str) => True or false
# left = 0
# right = 1 

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


def longestPalindromicSubstring(string):
    # time complexity: O(n^3)
    # space complexity: O(1)
    longest = ''

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest


def longestPalindromeEfficient(string):
    currentLongest = [0, 1] 

    for i in range(1, len(string)):
        odd = getLongestPalindrome(string, i - 1, i + 1)
        even = getLongestPalindrome(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0]: currentLongest[1]]

def getLongestPalindrome(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]

if __name__ == '__main__':
    print(longestPalindromicSubstring("abaxyzzyxf"))