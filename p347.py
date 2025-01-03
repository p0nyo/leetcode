def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dict = {} 
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 0


    # dict.items() puts dict into a list of tuples
    # lambda function makes sure the target key is the second element in the tuple
    sorted_dict = sorted(dict.items(), key=lambda x:x[1])
    sorted_dict.reverse()

    result = []

    for i in range(k):
        result.append(sorted_dict[i][0])

    return result

nums = [1,1,1,2,2,3]
k = 2

topKFrequent(nums, k)
