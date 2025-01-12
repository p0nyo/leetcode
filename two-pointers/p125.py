def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    lowercase_s = []

    for c in s:
        if ord(c) >= 65 and ord(c) <= 90:
            lowercase_s.append(c.lower())
        elif ord(c) >= 97 and ord(c) <= 122:
            lowercase_s.append(c)
        elif ord(c) >= 48 and ord(c) <= 57:
            lowercase_s.append(c)
        else:
            pass

    lowercase_s = "".join(lowercase_s)

    j = len(lowercase_s) - 1

    for i in range(len(lowercase_s)//2):
        if lowercase_s[i] != lowercase_s[j]:
            return False
        j -= 1

    return True


s = " "
print(isPalindrome(s))