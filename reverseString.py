# Question: Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# def reverseString(self, s):
    # input: list; output: string

    # Method 1: O(n)
    # s.reverse()

    # Method 2: O(n)
    # r, l = 0, len(s) - 1
    # while r < l:
    #     s[r], s[l] = s[l], s[r]
    #     r += 1
    #     l -= 1

        