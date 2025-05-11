# Question: Given a pattern and a string s, find if s follows the same pattern.
# Here follow the same pattern means a character in pattern can be mapped to a character in s.
# # Input: pattern = "abba", s = "dog cat cat dog"
# # Output: true
# # Input: pattern = "abba", s = "dog cat cat fish"
# # Output: false

# def wordPattern(self, pattern, s):
#     input: pattern, s; output: boolean

#     Method 1: O(n)
#     create two dictionaries to map pattern to s and s to pattern
#     loop through the pattern and s
#     if the pattern is already in the dictionary, check if the value is equal to s
#     if s is already in the dictionary, check if the value is equal to pattern
#     if both are not in the dictionary, add them to the dictionary

#     s = s.split(" ")
#     if len(pattern) != len(s):
#         return False

#     pattern_to_s = {}
#     s_to_pattern = {}

#     for i in range(len(pattern)):
#         if pattern[i] in pattern_to_s:
#             if pattern_to_s.get(pattern[i]) != s[i]:
#                 return False
#         if s[i] in s_to_pattern:
#             if s_to_pattern.get(s[i]) != pattern[i]:
#                 return False
#         pattern_to_s[pattern[i]] = s[i]
#         s_to_pattern[s[i]] = pattern[i]
#     return True