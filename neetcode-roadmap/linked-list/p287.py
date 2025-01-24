def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # loop through nums, get index from each num
    # mark it negative
    # if already negative return the number

    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            return abs(nums[index])
        nums[index] *= -1
    return None
    