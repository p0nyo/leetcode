class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicates = []
        for num in nums:
            if num not in duplicates:
                duplicates.append(num)
            else:
                return True
        return False

nums = [1,2,3,1]

print(Solution().containsDuplicate(nums))