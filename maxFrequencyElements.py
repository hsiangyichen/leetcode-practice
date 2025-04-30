# Question: Given a list of integers, return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# input: [1, 1, 2, 2, 3, 4]
# output: 4

# def maxFrequencyElements(self, nums):
    # input: list; output: num

    # Method 1: O(n^2)
    # loop through the list and find the frequency of each nums and find the max
    # if frequency > max, replace max and total
    # if frequency == max, total +=  frequency   
    # max_freq = 0
    # total = 0
    
    # for i in range(len(nums)):
    #     current_freq = 0
    #     for j in range(len(nums)):
    #         if nums[i] == nums[j]:
    #             current_freq += 1
        
    #     if current_freq > max_freq:
    #         max_freq = current_freq
    #         total = current_freq
    #     elif current_freq == max_freq:
    #         total += current_freq
            
    # return total // max_freq

    # return total 

    # Method 2: O(n)
    # build a dict and keep track of the max
    # loop through the dic and if value is max, total += value
    # nums_dict = defaultdict(int)
    # max_freq = 0
    # total = 0

    # for num in nums:
    #     nums_dict[num] += 1

    # for v in nums_dict.values():
    #     max_freq = max(max_freq, v)
    
    # for v in nums_dict.values():
    #     if v == max_freq:
    #         total += max_freq

    # return total