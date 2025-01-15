def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    L = 0
    R = len(height) - 1

    while L < R:
        area = (R-L) * min(height[L], height[R])
        if area > max_area:
            max_area = area

        if height[L] < height[R]:
            L += 1
        elif height[L] > height[R]:
            R -= 1
        else:
            L += 1
            R -= 1
    
    return max_area


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))