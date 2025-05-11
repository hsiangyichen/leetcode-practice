# Question: Given a string s which consists of letters, return the length of the longest palindrome that can be built with those letters.
# input: s = "abccccdd"
# output: 7

# def longestPalindrome(self, s):
    # input: str; output: num

    # Method 1: O(n!*n)
    # check every possible arrangement O(n!)
        # check if it’s a palindrome O(n)
        # keep track of the longest palindrome found

    # Method 2: O(n)
    # build a dict and check the value
    # add the even part of character frequencies
    # if there's at least one character with an odd count, we can place it in the center
    # s_dict = defaultdict(int)
    # result = 0
    # for i in range(len(s)):
    #     s_dict[s[i]] += 1
    # for v in s_dict.values():
    #     if v % 2 == 1:
    #         result += 1
    #         break
    # for v in s_dict.values():
    #     result += (v // 2) * 2
    # return result
        
        