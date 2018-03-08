#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice#.

#Example:
#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

nums = [2, 7, 11, 15]
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index in range(len(nums)):
            for index2 in range(len(nums)):
                if (nums[index] + nums[index2]  == target):
                    return list((index,index2))




a = Solution()
print (type(a.twoSum(nums,9)))
print(a.twoSum(nums,9))
print(nums)