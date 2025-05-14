# Question: Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# def searchInsert(self, nums, target):
    # input: 1 list, 1 num; output: int

    # Method 1: O(logn)
    # l, r = 0, len(nums) - 1
    # while l <= r:
    #     mid = (l + r) // 2
    #     if nums[mid] > target:
    #         r = mid - 1
    #     elif nums[mid] < target:
    #         l = mid + 1
    #     else:
    #         return mid
    # return l
        