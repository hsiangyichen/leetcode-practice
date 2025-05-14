# Question: Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Input: strs = ["dog","racecar","car"]
# Output: ""

# def longestCommonPrefix(self, strs):
    # start checking from the whole word of the first word with the other one's
    # if not strs:
    #     return ""
        
    # prefix = strs[0]

    # for word in strs:
    #     while not word.startswith(prefix):
    #         prefix = prefix[:-1]
    
    # return prefix