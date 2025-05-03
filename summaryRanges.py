# Question: Given a sorted integer array nums, return the smallest sorted list of ranges that cover all the numbers in the array exactly. Each range [a,b] in the list should be output as:
# a single string "a->b" if a != b, or just "a" if a == b.
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]

# def summaryRanges(self, nums):
    # input: list; output: list

    # Method 1: O(n)
    # loop through the list and add the num to string
    # if next num is not continuous, append the string to the result
    # if not nums:
    #     return []

    # ranges, range_num = [], []
    # nums.append(nums[-1])

    # for i in range(len(nums)):
    #     range_num.append(nums[i])
    #     if i + 1 < len(nums) and nums[i] + 1 != nums[i+1]:
    #         if range_num[0] != range_num[-1]:
    #             ranges.append(str(range_num[0]) + "->" + str(range_num[-1]))
    #         else:
    #             ranges.append(str(range_num[0]))
    #         range_num = []

    # return ranges
        
    