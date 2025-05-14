# Question: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

# def sortedSquares(self, nums):

    # input: list; output: list
    # Method 1: O(n)
    # result = []
    # l, r = 0, len(nums) - 1
    # while l <= r:
    #     if nums[l]**2 > nums[r]**2:
    #         result.append(nums[l]**2)
    #         l += 1
    #     else:
    #         result.append(nums[r]**2)
    #         r -= 1
    # return result[::-1]
        