# Question: Given an integer array nums of size n, return the majority element.
# The majority element is the element that appears more than n / 2 times. You may assume that the majority element always exists in the array.
# Input: nums = [3,2,3]
# Output: 3

# def majorityElement(self, nums):
    # input: list; output: num

    # Method 1: O(n^2)
    # n = len(nums)
    # for i in range(n):
    #     count = 0
    #     for j in range(n):
    #         if nums[j] == nums[i]:
    #             count += 1
    #     if count > n // 2:
    #         return nums[i]

    # Method 2: O(nlogn)
    # nums.sort()
    # majority = nums[len(nums) / 2]
    # return majority
            

        

        