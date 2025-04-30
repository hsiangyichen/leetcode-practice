# Question: Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# input: [1, 2, 3, 1], k = 3
# output: true

# def containsNearbyDuplicate(self, nums, k):
    # input: 1 list, 1 num; output: boolean
    
    # Method 1: O(n^2)
    # loop through the list and compared with all the dist <= k
    # for i in range(len(nums)):
    #     for j in range(i+1, min(i+k+1, len(nums))):        
    #         if nums[i] == nums[j]:
    #             return True
    # return False

    # Method 2: O(n)
    # loop through the set to check if there is duplicates
        # if yes, return true
        # add it to the set
        # if the window is too big, replace the window size
    # nums_set = set()
    # for i in range(len(nums)):
    #     if len(nums_set) > k:
    #         nums_set.remove(nums[i-k-1])
    #     if nums[i] in nums_set:
    #         return True
    #     nums_set.add(nums[i])
        
    # return False

    # Method 3: O(n)
    # loop through the dict to check if there is duplicates
        # if yes, check if that value - curr value <= k
            # if yes, return true
    # add it to the dict
    # nums_dict = {}
    # for i in range(len(nums)):
    #     if nums[i] in nums_dict and i - nums_dict[nums[i]] <= k:
    #         return True
    #     nums_dict[nums[i]] = i
    # return False

    