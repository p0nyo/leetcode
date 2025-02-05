def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    l = 0
    max_len = 0
    string_set = set(s[r])

    for r in range(len(s)):
        while s[r] in string_set:
            string_set.remove(s[r])
            l += 1
        string_set.add(s[r])
        max_len = max(max_len, r - l + 1)
        
    return max_len

s = "abcabcbb"
s = "anviaj"
print(lengthOfLongestSubstring(s))
