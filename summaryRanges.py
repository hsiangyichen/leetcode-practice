# Question: Given a sorted integer array nums, return the smallest sorted list of ranges that cover all the numbers in the array exactly. Each range [a,b] in the list should be output as:
# a single string "a->b" if a != b, or just "a" if a == b.
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]

# def summaryRanges(self, nums):
    # input: list; output: list

    # Method 1: O(n)
    # loop through the list and add the num to string
    # if curr num is not continuous, append the string of start and the prev num to the result
    # if not nums:
    #     return []
    # result = []
    # nums.append(nums[-1])

    # start = nums[0] # 0
    # for i in range(1, len(nums)):
    #     if nums[i] != nums[i-1] + 1:
    #         if start == nums[i-1]:
    #             result.append(str(start))
    #         else:
    #             result.append(str(start) + "->" + str(nums[i - 1]))
    #         start = nums[i]
    # return result