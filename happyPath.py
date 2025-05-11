# Question: Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process: Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, and repeat the process until the 
# number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1. 
# Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.

# Input: n = 19
# Output: true

# Explanation: 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# Hence, n is a happy number.

# def isHappy(self, n):
    # Method 1: O(n^2)
    # check if n is in the seen list
    # if yes, return false
    # if no, add n to the seen list
    # loop through the digits of n and sum the square of each digit
    # if the sum is 1, return true

    # seen = []
    # while n != 1 and n not in seen:
    #     seen.append(n)
    #     sum = 0
    #     for digit in str(n):
    #         sum += int(digit) ** 2
    #     print(sum)   
    #     n = sum
    # return n == 1

    # Method 2: O(n)
    # check if n is in the seen set
    # if yes, return false
    # if no, add n to the seen set
    # loop through the digits of n and sum the square of each digit
    # if the sum is 1, return true

    # seen = set()
    # while n != 1:
    #     if n in seen:
    #         return False
    #     seen.add(n)
    #     new_n = 0
    #     for digit in str(n):
    #         new_n += int(digit)**2
    #     n = new_n
    # return True