# Question: Given two binary strings a and b, return their sum as a binary string.

# Input: a = "11", b = "1"
# Output: "100"
# Input: a = "1010", b = "1011"
# Output: "10101"

# def addBinary(self, a, b):

    # Method 1: O(n)
    # loop through the binary strings from the end
    # check if the sum of the two bits and carry is greater than 1
    # if yes, set carry to 1 and digit to 0
    # if no, set carry to 0 and digit to 1
    # append the digit to the result
    # if there is still carry left, append it to the result
    # reverse the result and join it to return the final string

    # i = len(a) - 1
    # j = len(b) - 1
    # carry = 0
    # result = []

    # while i >= 0 or j >= 0 or carry > 0:
    #     bitA = a[i] if i >= 0 else 0
    #     bitB = b[j] if j >= 0 else 0

    #     digit_sum = int(bitA) + int(bitB) + carry
    #     digit = digit_sum % 2
    #     carry = digit_sum // 2

    #     result.append(str(digit))

    #     i -= 1
    #     j -= 1

    # return "".join(result[::-1])