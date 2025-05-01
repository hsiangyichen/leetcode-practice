# Question: Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# def reverseWords(self, s):
    # input: string; output: string

    # Method 1: O(n^2)
    # make it a list by separate it by space
    # reverse each word and join them
    # s = s.split(" ")
    # sentence = ""

    # for i in range(len(s)):
    #     sentence += s[i][::-1]
    #     if i < len(s) - 1:
    #         sentence += " "
    
    # return sentence
    
    # Method 2: O(n)
    # s = s.split(" ")
    # sentence = []

    # for word in s:
    #     sentence.append(word[::-1])
    
    # return " ".join(sentence)


        