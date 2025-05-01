# Question: Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.
# If no such index exists, return -1. If there are multiple pivot indexes, you should return the leftmost pivot index.
# Input: nums = [1,7,3,6,5,6]
# Output: 3
 
# def pivotIndex(self, nums):
    # input: list; output: num

    # Method 1: O(n^2)
    # loop through the list and set the each index as the pivot
        # add up the leftsum and rightsum and check which one leftsum == rightsum
        # if yes, return that index
        # if no, return -1

    # Method 2: O(n)
    # leftSum, rightSum = 0, sum(nums)
    # for i, v in enumerate(nums):
    #     rightSum -= v
    #     if leftSum == rightSum:
    #         return i
    #     leftSum += v
    # return -1