# Question: Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4

# def search(self, nums, target):
    # l, r = 0, len(nums) - 1
    # while l <= r:
    #     mid = (l + r) // 2 
    #     if nums[mid] < target:
    #         l = mid + 1
    #     elif nums[mid] > target:
    #         r = mid - 1
    #     else:
    #         return mid
    # return -1