# Question: Given an integer x, return true if x is a palindrome, and false otherwise.
# Input: x = 121
# Output: true

# def isPalindrome(self, x):
    # input: num; output: boolean

    # Method 1: O(n)
    # make it a list and use two pointer (l and r) until the center
    # check if x[l] == x[r]
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
    # check if x is negative or if the last digit is 0; if yes, return false
    # reverses the last half of the digits of x and compare it with the first half
    # if x < 0 or (x % 10 == 0 and x != 0):
    #     return False
    # reverted = 0
    # while x > reverted:
    #     reverted = reverted * 10 + x % 10
    #     x = x // 10
    # return x == reverted or x == reverted // 10

