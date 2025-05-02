# Question: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# def moveZeroes(self, nums):

    # Method 1: O(n^2)
    # count = 0
    # while 0 in nums:
    #     count += 1
    #     nums.remove(0)
    
    # for i in range(0, count):
    #     nums.append(0)
    
    # Method 2: O(n)
    # j = 0
    # for i in range(len(nums)):        
    #     if nums[i] != 0:
    #         nums[j] = nums[i]
    #         j += 1
    # for i in range(j,len(nums)):
    #     nums[i] = 0

    # method 3: O(n)
    # j = 0
    # for i in range(len(nums)):        
    #     if nums[i] != 0:
    #         nums[j], nums[i] = nums[i], nums[j]
    #         j += 1

    