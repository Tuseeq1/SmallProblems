"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, val in enumerate(nums):
            index2 = index
            second_val = target - val
            if second_val in nums:
                index2 = nums.index(second_val)

            if index != index2:
                return [index, index2]
