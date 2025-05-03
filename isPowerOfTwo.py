# Question: Given an integer n, return true if it is a power of two. Otherwise, return false.
# Input: n = 16
# Output: true
# Input: n = 3
# Output: false

# def isPowerOfTwo(self, n):
    
    # Method: O(logn)
    # use the fact that a number is a power of 2 if it can be divided by 2 until it reaches 1
    # while n > 1:
    #     n = n / 2.0
    # return n == 1

    # Method 2: O(1)
    # use the fact that a number is a power of 2 if it is greater than 0 and n & (n - 1) == 0
    # return n > 0 and n & (n - 1) == 0
        