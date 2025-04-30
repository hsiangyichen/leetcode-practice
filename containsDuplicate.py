class Solution(object):
    def containsDuplicate(self, nums):
        # input: list; output: boolean

        # Method 1: O(n^2)
        # loop through the list and see if that number also in the rest of the list     
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Method 2: O(n)
        # build a dict and loop through the values to see if there is num larger than 1
        # nums_dict = defaultdict(int)
        # for i in range(len(nums)):
        #     nums_dict[nums[i]] += 1
        
        # for v in nums_dict.values():
        #     if v > 1:
        #         return True
        # return False

        # Method 3: O(n)
        # Counter
        # for v in Counter(nums).values():
        #     if v > 1:
        #         return True
        # return False

        # Method 4: O(n)
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # Method 5: O(n)
        # return len(nums) != len(set(nums))