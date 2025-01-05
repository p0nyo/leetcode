def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = [0] * len(nums)
    prefix = [0] * len(nums)
    suffix = [0] * len(nums)

    prefix[0] = 1
    suffix[len(nums) - 1] = 1
    print(suffix)

    for i in range(1,len(nums)):
        prefix[i] = nums[i-1] * prefix[i-1]

    for i in range(len(nums)-2, -1, -1):
        print(i)
        suffix[i] = nums[i+1] * suffix[i+1]

    for i in range(len(nums)):
        result[i] = prefix[i] * suffix[i]
        
    return result


nums = [1,2,3,4]

print(productExceptSelf(nums))