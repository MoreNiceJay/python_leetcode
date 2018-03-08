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

        dict = {}
        t=0
        for i in range(len(nums)):

            complement = target - nums[i]
            if nums[i] in dict.keys():
                return(i,dict[nums[i]])
            dict[complement] = i








a = Solution()
print (a.twoSum(nums,99))








# dict = {}
# for i in range(len(nums)):
#     complement = target - nums[i]
#     if (nums[i] in dict.keys()):
#         print('Current index: ', i, ' Other index: ', dict[nums[i]])
#     dict[complement] = i
#     print(i)
# print(dict)