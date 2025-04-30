# Question: Given an integer x, return true if x is a palindrome, and false otherwise.
# Input: x = 121
# Output: true

# def isPalindrome(self, x):
    # input: num; output: boolean

    # Method 1: O(n)
    # make it a list and use two pointer (l and r) until the center
    # check if list_x[l] == list_x[r]
    # x = list(str(x))
    # l, r = 0, len(x) - 1
    # while l < r:
    #     if x[l] != x[r]:
    #         return False
    #     l += 1
    #     r -= 1
    # return True

    # Method 2: O(n)
    # x = str(x)
    # return x == x[::-1]

    # Method 3: O(logn)
    # if x < 0 or (x % 10 == 0 and x != 0):
    #     return False
    # reverted = 0
    # while x > reverted:
    #     reverted = reverted * 10 + x % 10
    #     x //= 10
    # return x == reverted or x == reverted // 10

