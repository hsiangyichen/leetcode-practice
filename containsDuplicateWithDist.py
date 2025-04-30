# Question: If i want to return true if two nums are the same and their distance is k, how can i do that?
# input: [1, 2, 3, 1], k = 3
# output: true

# def containsDuplicateWithDist(self, nums, k):
    # input: 1 list, 1 num; output: boolean

    # Method 1: O(n^2)
    # loop through all the pairs and see if any of their dist is == k
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] == nums[j] and j - i == k:
    #             return True
    # return False

    # Method 2: O(n)
    # build a dict and store the dist
    # check if any value == k
    # nums_dict = {}
    # for i in range(len(nums)):
    #     num = nums[i]
    #     if num in nums_dict:
    #         if i - nums_dict[num] == k:
    #             return True
    #     nums_dict[num] = i
    # return False

    # Method 3: O(n)
    # loop the list
    # check if nums[j] == nums[j+3]      
    # j = 0
    # while j + k < len(nums):
    #     if nums[j] == nums[j+k]:
    #         return True
    #     j += 1
    # return False
    