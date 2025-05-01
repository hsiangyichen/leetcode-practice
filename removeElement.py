# Question: Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]

# def removeElement(self, nums, val):
    # input: 1 list, 1 num; output: num

    # Method 1: O(n^2)
    # while val in nums:
    #     nums.remove(val)
    # return len(nums)

    # Method 2: O(n)
    # k = 0
    # for i in range(len(nums)):
    #     if nums[i] != val:
    #         nums[k] = nums[i]
    #         k += 1
    # return k

