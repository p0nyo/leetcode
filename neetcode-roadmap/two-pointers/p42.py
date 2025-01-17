def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height) - 1
    maxL, maxR = height[l], height[r]
    res = 0

    while l < r:
        if maxL <= maxR:
            l += 1
            water = maxL - height[l]
            if water > 0:
                res += water
            if height[l] > maxL:
                maxL = height[l]
        else:
            r -= 1
            water = maxR - height[r]
            if water > 0:
                res += water
            if height[r] > maxR:
                maxR = height[r]
    
    return res

# def trap2(height):

height = [3,0,4,0,3]
print(trap(height))