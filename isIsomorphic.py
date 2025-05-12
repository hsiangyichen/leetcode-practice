# Question: Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
# Input: s = "egg", t = "add"
# Output: true
# Input: s = "foo", t = "add"
# Output: false

# def isIsomorphic(self, s, t):
    # input: 2 strings; output: boolean

    # Method 1: O(n)
    # loop through both strings
    #     if the char is already in the dictionary, check if the value is equal to the other string 
    #     if both are not in the dictionary, add them to the dictionary

    # if len(s) != len(t):
    #     return False

    # s_to_t = {}
    # t_to_s = {}

    # for i in range(len(s)):
    #     if s[i] in s_to_t:
    #         if s_to_t.get(s[i]) != t[i]:
    #             return False
    #     if t[i] in t_to_s:
    #         if t_to_s.get(t[i]) != s[i]:
    #             return False
    #     s_to_t[s[i]] = t[i]
    #     t_to_s[t[i]] = s[i]
    # return True