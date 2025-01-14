def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()

    print(nums)
    
    for i, num in enumerate(nums):
        # end iteration if:
        # 1. num is the same value as one before
        # 2. num is greater than 0, means we can't make 0 since list is sorted in ascending order
        if i > 0:
            if num > 0 or num == nums[i-1]:
                # print(num, i-1)
                continue
        
        j, k = i+1, len(nums) - 1
        # print(j,k)
        print("start:", j, nums[j], k, nums[k])
        while j < k:
            three_sum = num + nums[j] + nums[k]
            if three_sum > 0:
                print(j, nums[j], k, nums[k])
                k -= 1
            elif three_sum < 0:
                j += 1
            else:
                res.append([num, nums[j], nums[k]]) 
                j += 1
                k -= 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1
    return res



nums = [-1,0,1,2,-1,-4]
nums1 = [0,0,0]
nums2 = [-2,0,0,2,2]
nums3 = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

# target = 0

print(threeSum(nums3))