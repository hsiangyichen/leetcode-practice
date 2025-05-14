# Question: Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# The relative order of items in arr1 will be the same as their relative order in arr2.
# Elements that do not appear in arr2 should be placed at the end of arr1 in arbitrary order.

# Input: arr1 = [2,1,2,5,3], arr2 = [5,3]
# Output: [5,3,2,1,2]

# def relativeSortArray(self, arr1, arr2):
    # arr1_dict = Counter(arr1)
    # result = []

    # for num in arr2:
    #     if num in arr1:
    #         result.extend([num]*arr1_dict[num])
    #         del arr1_dict[num]
    # extra = sorted(arr1_dict)
    # for num in extra:
    #     result.extend([num]*arr1_dict[num])

    # return result