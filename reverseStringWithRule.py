# Question: Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string. 
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
# then reverse the first k characters and leave the other as original.
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# def reverseStr(self, s, k):
    # input: 1 string, 1 num; output: string
    
    # Method 1: O(n^2)
    # for every 2k char
        # insert the reverse k char and insert the other k char without reverse

    # j = 0
    # result_s = ""

    # while j < len(s): # O(n)
    #     result_s = result_s + s[j:j+k][::-1] + s[j+k:j+2*k] # O(n)
    #     j += 2*k
    # return result_s

    # Method 2: O(n)
    # for every 2k char
        # append the reverse k char and append the other k char without reverse
    # j = 0
    # result_s = []

    # while j < len(s): # O(n)
    #     result_s.append(s[j:j+k][::-1])
    #     result_s.append(s[j+k:j+2*k])
    #     j += 2*k
    # return "".join(result_s)


    