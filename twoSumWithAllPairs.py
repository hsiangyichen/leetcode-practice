# Question: If i want to return the index of all the pairs that add up to the target, how can i do that?
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