# Question: Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# A word is defined as a character sequence consists of non-space characters only.
# Input: s = "Hello World"
# Output: 5

# def lengthOfLastWord(self, s):
    # input: string; output: num

    # Method 1: O(n^2)
    # make the string into a list
    # get the last value of the list
    # return the length of that value

    # s = s.split(" ")
    # while "" in s: # O(n)
    #     s.remove("") # O(n)

    # return len(s.pop())

    # Method 2: O(n)
    # s = s.split(" ")
    # for word in reversed(s):
    #     if word != "":
    #         return len(word)

    # Method 3: O(n)
    # s = s.strip().split()
    # return len(s[-1])