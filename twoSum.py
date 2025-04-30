# Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

# def twoSum(self, nums, target):
    # input: 1 list, 1 num; output: list

    # Method 1: O(n^2)
    # loop through the list
        # loop through the rest of the num
            # check which two nums = target
                # if found, append them to the list
    # return the list

    # Method 2: O(nlogn)
    # build a dict for the list first
    # sort the list
    # use two pointer from the left and the right to loop through the list
    # add two nums together and check if it is larger than target
        # if yes, move the right pointer
        # if no, move the left pointer
    # find the corresponding value of these two pointer
    # return the list

    # Method 3: O(n)
    # build a dict for the list
    # loop through the key and find the complement of those num
        # check if the complement is also in the key
        # if yes, append their corresponding value to the list
    # return the list

