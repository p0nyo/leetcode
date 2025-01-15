def carFleet(target, position, speed):
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """

    stack = []

    for i in range(len(position)):
        position_i = position[i]
        position[i] = (position_i, speed[i])

    sorted_positions = sorted(position, key=lambda x:x[0])
    sorted_positions.reverse()

    for pos in sorted_positions:
        current_time = (target-pos[0]) / pos[1]
        if stack and current_time <= stack[-1][0]:
            top_time = stack.pop()
            top_time.append(current_time)
            stack.append(top_time)
        else:
            stack.append([current_time])
    
    return len(stack)



# target = 12
# position = [10,8,0,5,3]
# speed = [2,4,1,1,3]

target = 10
position = [6,8]
speed = [3,2]

print(carFleet(target, position, speed))