def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """

    # dictionary to store character + frequency
    # left and right pointer starts at 0, 0 
    char_set = set(s)
    res = 0

    for c in char_set:
        count = l = 0
        for r in range(len(s)):
            if s[r] == c:
                count += 1
            
            while (r-l+1) - count > k:
                if s[l] == c:
                    count -= 1
                
                l += 1
            
            res = max(res, r-l+1)

    return res
    
s = "ABAB"
k = 2

print(characterReplacement(s,k))

