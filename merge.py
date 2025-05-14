# Question: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# def merge(self, nums1, m, nums2, n):

    # input: 2 lists, 2 ints; output: list
    # Method 1: O(m+n)
    # i = m - 1
    # j = n - 1
    # k = m + n - 1

    # while j >= 0:
    #     if i >= 0 and nums2[j] < nums1[i]:
    #         nums1[k] = nums1[i]
    #         i -= 1
    #     else:
    #         nums1[k] = nums2[j]
    #         j -= 1     
    #     k -= 1