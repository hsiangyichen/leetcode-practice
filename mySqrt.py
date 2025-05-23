# Question: Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Input: x = 4
# Output: 2
# Input: x = 8
# Output: 2

# def mySqrt(self, x):

    # Method 1: O(x^(1/2))
    # check if the square of the (power+1) is less than or equal to x
    # if it is, increase the power by 1
    # if not, return the power
    # power = 0
    # while (power+1) * (power+1) <= x: 
    #     power += 1

    # return power

    # Method 2: O(logn) binary search
    # check if the square of the mid is greater than x, if it is, move the right pointer to mid - 1
    # check if the square of the mid is less than x, if it is, move the left pointer to mid + 1
    # check if the square of the mid is equal to x, if it is, return mid
    # if not, return the right pointer
    # l, r = 0, x
    # while l <= r:
    #     mid = (l+r) // 2
    #     if mid * mid < x: 
    #         l = mid + 1
    #     elif mid * mid > x:
    #         r = mid - 1
    #     else:
    #         return mid
    # return r