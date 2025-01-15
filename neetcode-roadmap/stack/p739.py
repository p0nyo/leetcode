def dailyTemperatures(temperatures):
    # init a result list
    # init a stack list
    # for loop through temperatures, if value is larger than what is on stack, pop
    # if not, push it
    # use while loop to achieve that

    res = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        temperature = temperatures[i]
        index = i
        while len(stack) != 0 and temperature > stack[-1][0]:
            _, res_index = stack.pop()
            res[res_index] = index - res_index
        stack.append((temperature, index))
    return res


# trying with enumerate
def dailyTemperaturesV2(temperatures):
    # init a result list
    # init a stack list
    # for loop through temperatures, if value is larger than what is on stack, pop
    # if not, push it
    # use while loop to achieve that

    res = [0] * len(temperatures)
    stack = []

    for index, temperature in enumerate(temperatures):
        while len(stack) != 0 and temperature > stack[-1][0]:
            _, res_index = stack.pop()
            res[res_index] = index - res_index
        stack.append((temperature, index))
    return res



temperatures = [73,74,75,71,69,72,76,73]
temperatures2 = [2,1,1,3]

print(dailyTemperaturesV2(temperatures2))