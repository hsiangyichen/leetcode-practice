# Question: Given an integer array nums of size n, return the majority element.
# The majority element is the element that appears more than n / 2 times. You may assume that the majority element always exists in the array.
# Input: nums = [3,2,3]
# Output: 3

# def majorityElement(self, nums):
    # input: list; output: num

    # Method 1: O(n^2)
    # loop through the list and see if that number also in the rest of the list
        # check if the count of that number is larger than n/2
        # if yes, return that number
    # for i in range(len(nums)):
    #     count = 0
    #     for j in range(len(nums)):
    #         if nums[j] == nums[i]:
    #             count += 1
    #     if count > n // 2:
    #         return nums[i]

    # Method 2: O(nlogn)
    # sort the list first
    # return the middle element
    # nums.sort()
    # majority = nums[len(nums) / 2]
    # return majority
            

        

        