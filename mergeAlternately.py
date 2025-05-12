# Question: You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"

# def mergeAlternately(self, word1, word2):
    # input: 2 strings; output: string

    # Method 1: O(n+m)
    # result = []
    # i, j = 0, 0
    # while i < len(word1) or j < len(word2):
    #     if i < len(word1):
    #         result.append(word1[i])
    #     if j < len(word2):
    #         result.append(word2[j])
    #     i += 1
    #     j += 1
    # return "".join(result)