# Question: Given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

# Input: nums1 = [1,2,3], nums2 = [2,3,4]
# Output: 2
# Input: nums1 = [1,2,3], nums2 = [4,5,6]
# Output: -1

# def getCommon(self, nums1, nums2):

    # input: 2 lists; output: int
    # Method 1: O(n^2)
    # for num1 in nums1:
    #     for num2 in nums2:
    #         if num1 == num2:
    #             return num1
    # return -1

    # Method 2: O(n)
    # nums2 = set(nums2)
    # for num1 in nums1:
    #     if num1 in nums2:
    #         return num1
    # return -1