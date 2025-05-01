# Question: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

# def strStr(self, haystack, needle):

    # Method 1: O(n*m)
    # check all the sub string
    # for i in range(len(haystack)-len(needle)+1):
    #     if haystack[i:i+len(needle)] == needle:
    #         return i
    # return -1

    # Method 2: O(n)
    # return haystack.find(needle)
        