def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []

    for token in tokens:
        # If token is integer
        try:
            int_token = int(token)
            stack.append(int_token)
        # If token is operator
        except ValueError:
            param1 = stack.pop()
            param2 = stack.pop()

            if token == "*":
                stack.append(param2 * param1)
            elif token == "-":
                stack.append(param2 - param1)
            elif token == "+":
                stack.append(param2 + param1)
            elif token == "/":
                stack.append(int(float(param2) / param1))
            
    return stack[-1]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))
