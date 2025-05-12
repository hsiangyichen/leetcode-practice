# Question: Given two strings s and t, which consist of lowercase letters only, return the letter that was added to t.
# Input: s = "abcd", t = "abcde"
# Output: "e"

# def findTheDifference(self, s, t):

    # Method 1: O(m*n)
    # s = list(s)
    # for c in t:
    #     if c not in s:
    #         return c
    #     else:
    #         s.remove(c)

    # Method 2: O(n+m)
    # s = Counter(s)
    # for c in t:
    #     if c in s and s[c] != 0:
    #         s[c] -= 1
    #     else:
    #         return c

    # Method 3: O(n)
    # s_sum = sum(ord(x) for x in s)
    # t_sum = sum(ord(y) for y in t)

    # return chr(t_sum - s_sum)
        


    