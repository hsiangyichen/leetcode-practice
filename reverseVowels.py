# Question: Given a string s, reverse only all the vowels in the string and return it.

# Input: s = "hello"
# Output: "holle"  

# Input: s = "leetcode"
# Output: "leotcede"  

# def reverseVowels(self, s):
    # input: string; output: string

    # Method 1: O(n^2)

    # vowels = "AEIOUaeiou"
    # result = ""
    # s_vowels = []
    # for i in range(len(s)):
    #     if s[i] in vowels:
    #         s_vowels.append(s[i])
    # for i in range(len(s)):
    #     if s[i] not in vowels:
    #         result += s[i]
    #     else:
    #         result += s_vowels.pop()
    # return result

    # Method 2: O(n)

    # vowels = "AEIOUaeiou"
    # result = []
    # s_vowels = []
    # for i in range(len(s)):
    #     if s[i] in vowels:
    #         s_vowels.append(s[i])
    # for i in range(len(s)):
    #     if s[i] not in vowels:
    #         result.append(s[i])
    #     else:
    #         result.append(s_vowels.pop())
    # return "".join(result)