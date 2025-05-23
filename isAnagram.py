# Question: Given two strings s and t, return true if t is an anagram of s and false otherwise.
# Input: s = "anagram", t = "nagaram"
# Output: true

# def isAnagram(self, s, t):
    # input: 2 strings; output: boolean

    # Method 1:
    # loop through the first str and turn it into a dict
    # loop through the second str and turn it into a dict
    # check if any value is different
        # if yes, return false
    # return true

    # Method 2: O(n)
    # loop through both strings
        # if it is from t, +1
        # if it is from s, -1
    # check if all the value is 0
        # if not, return false
    # return true

    # Method 3: O(n)
    # use Counter
    # return Counter(s) == Counter(t) 