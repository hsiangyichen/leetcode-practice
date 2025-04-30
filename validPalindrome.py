# Question: Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Input: s = "abca"
# Output: true

# def validPalindrome(self, s):
    # input: string; output: boolean

    # Method 1: O(n^2)
    # check all the possible arrangement of s
    # "aba", "ba","aa", "ab"
    # if any arrangement == the reverse of it, return true
    # for i in range(len(s)):
    #     modified = s[:i] + s[i+1:] # O(n)
    #     if modified == modified[::-1]:
    #         return True

    # return False

    # Method 2: O(n)
    # use two pointers (left and right) to compare characters
    # if there is a mismatch, remove one character and check if the rest is a palindrome
    # def is_palindrome(sub):
    #     return sub == sub[::-1]
    
    # left, right = 0, len(s) - 1

    # while left < right:
    #     if s[left] != s[right]:
    #         return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
    #     left += 1
    #     right -= 1

    # return True


