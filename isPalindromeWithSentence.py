# Question: Given a string, determine if it is a palindrome.
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# def isPalindrome(self, s):
    # input: string, output: boolean
    
    # Method 1: O(n^2)
    # remove all the space and special char and turn them into lower case
    # insert the char to build a reverse str of s
    # s = ''.join(c for c in s if c.isalnum()).lower()
    # reversed_s = ""
    # for c in s:
    #     reversed_s = c + reversed_s
    # return s == reversed_s

    # Method 2: O(n)
    # remove all the space and special char and turn them into lower case
    # make a reverse copy of s
    # s = ''.join(c for c in s if c.isalnum()).lower()
    # return s == s[::-1]
    
    