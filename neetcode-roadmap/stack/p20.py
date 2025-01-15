def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # for loop with a stack ds

    bracket_dict = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    stack = []

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]" and len(stack) == 0:
            return False
        elif bracket_dict[stack.pop()] != char:
            return False
    
    if len(stack) == 0:
        return True
    return False

            

s = ']'

print(isValid(s))