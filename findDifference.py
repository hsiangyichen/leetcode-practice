# Question: Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of distinct integers in nums1 which are not present in nums2
# answer[1] is a list of distinct integers in nums2 which are not present in nums1
# The values in the two lists should be returned in any order.
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]

# def findDifference(self, nums1, nums2):
    # input: 2 lists; output: 2d array
    
    # Method 1: O(n^2)
    # distinct_nums1 = []
    # distinct_nums2 = []
    # for num1 in nums1:
    #     if num1 not in nums2:
    #         distinct_nums1.append(num1)
    # for num2 in nums2:
    #     if num2 not in nums1:
    #         distinct_nums2.append(num2)
    # return list(set(distinct_nums1)), list(set(distinct_nums2))

    # Method 2: O(n)
    # set1, set2 = set(nums1), set(nums2)
    # return list(set1-set2), list(set2-set1)
    