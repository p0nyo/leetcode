def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """    
    # turn array into hash set
    numSet = set(nums)
    longest = 0

    # loop through set to find element that has potential to be the beginning of a sequence
    for num in numSet:
        if num-1 not in numSet:
            length = 1
            while num + 1 in numSet:
                length += 1
                num += 1
            longest = max(longest, length)
    return longest

            

nums = [100,4,200,1,3,2]

print(longestConsecutive(nums))