# Question: Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Input: arr = [1,2,2,1,1,3]
# Output: true

# def uniqueOccurrences(self, arr):
    # input: list; output: boolean

    # Method 1: O(n^2)
    # build a dict
    # check if there is duplicated value
    # if yes, return false
    # arr_dict = defaultdict(int)
    # for value in arr:
    #     arr_dict[value] += 1
    # arr_list = []
    # for v in arr_dict.values():
    #     arr_list.append(v)
    # print(arr_list)
    # for i in range(len(arr_list)):
    #     for j in range(i+1, len(arr_list)):
    #         if arr_list[i] == arr_list[j]:
    #             return False
    # return True

    # Method 2: O(n)
    # arr_dict = defaultdict(int)
    # for value in arr:
    #     arr_dict[value] += 1
    # occurrences = arr_dict.values()
    # return len(occurrences) == len(set(occurrences))

    # Method 3: O(n)
    # occurrences = Counter(arr).values()
    # return len(occurrences) == len(set(occurrences))
        


