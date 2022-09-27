def are_anagrams(string1, string2):
    # time complexity: O(n)
    # space complexity: O(n)
    
    if len(string1) != len(string2):
        return False
    freq1 = {}
    freq2 = {}

    for ch in string1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    
    for ch in string2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    
    return True