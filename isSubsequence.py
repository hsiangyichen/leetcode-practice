# Question: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Input: s = "axc", t = "ahbgdc"
# Output: false

# def isSubsequence(self, s, t):
    # input: 2 string; output: boolean
    

    # Method 1: O(m * n)
    # loop through s and t and check if there is a match
    # use count to kee track of the matched char
    # if yes, update j and break
    # if no, update j 

    # if len(s) > len(t):
    #     return False
    # count = 0
    # j = 0
    # for i in range(len(s)):
    #     while j < len(t):
    #         if s[i] == t[j]:
    #             count += 1
    #             j += 1
    #             break
    #         j += 1
    # return count == len(s)

    # Method 2: O(n)
    # loop through s and t and check if there is a match
    # if yes, update i
    # move both pointer
    # if i goes till the end, means it is a subsequence 
    # i, j = 0, 0
    # while i < len(s) and j < len(t):
    #     if s[i] == t[j]:
    #         i += 1
    #     j += 1
    # return i == len(s)