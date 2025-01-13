def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    i = 0
    j = len(numbers) - 1

    while True:
        if numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            return [i+1,j+1]
        
numbers = [-1,0]
target = -1

print(twoSum(numbers, target))
