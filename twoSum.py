class Solution(object):
    def twoSum(self, nums, target):
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

# Related Question: if i want to return the index of all the pairs that add up to the target, how can i do that?
# input: [1, 2, 3, 3, 4, 5], target = 5
# output: [[0, 4], [1, 2], [1, 3]]

# def two_sum_index_pairs(nums, target):
#     index_map = {}
#     result = []

#     for i in range(len(nums)):
#         num = nums[i]
#         complement = target - num

#         if complement in index_map:
#             for j in index_map[complement]:
#                 result.append([j, i])

#         if num in index_map:
#             index_map[num].append(i)
#         else:
#             index_map[num] = [i]

#     return result

