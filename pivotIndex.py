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
    # for i in range(len(nums)):
    #     leftsum, rightsum = 0, 0
    #     for j in range(0, i):
    #         leftsum += nums[j]
    #     for j in range(i+1, len(nums)):
    #         rightsum += nums[j]
    #     if leftsum == rightsum:
    #         return i
    # return -1

    # Method 2: O(n)
    # leftsum, rightsum = 0, sum(nums)
    # for i in range(len(nums)):
    #     rightsum -= nums[i]
    #     if leftsum == rightsum:
    #         return i
    #     leftsum += nums[i]
    # return -1