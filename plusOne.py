# Question: You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Input: digits = [9]
# Output: [1,0]


# def plusOne(self, digits):
    # input: list; output: list
    
    # Method 1: O(n)
    # nums = 1
    # digits = digits[::-1]
    # result = []
    # for i in range(len(digits)):
    #     nums += digits[i]*(10**i)
    # for num in str(nums):
    #     result.append(int(num)) 
    # return result

    # Method 2: O(n)
    # j = len(digits) - 1
    # digits[-1] += 1
    # while j >= 0 and digits[j] > 9:
    #     digits[j] = 0
    #     if j == 0:
    #         digits.insert(0,1) # will only called once
    #         break
    #     else:
    #         digits[j-1] += 1
    #     j -= 1         
    # return digits
        
        