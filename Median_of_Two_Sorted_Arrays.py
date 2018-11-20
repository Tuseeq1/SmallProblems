"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = n2 = 0
        nums = []
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] < nums2[n2]:
                nums.append(nums1[n1])
                n1 += 1
            else:
                nums.append(nums2[n2])
                n2 += 1
        while n1 < len(nums1):
            nums.append(nums1[n1])
            n1 += 1
        while n2 < len(nums2):
            nums.append(nums2[n2])
            n2 += 1
        print(nums)
        mid=int(len(nums)/2)
        if len(nums)%2 != 0:
            return nums[mid]
        else:
            return (nums[mid]+nums[mid-1])/2