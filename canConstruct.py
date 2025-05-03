# Question: Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# def canConstruct(self, ransomNote, magazine):

    # Method 1: O(n*m)
    # loop through the ransomNote
        # see if char is in magazine
        # if yes, remove the char in magazine
        # if no, return False
    # magazine = list(magazine)
    # for char in ransomNote:
    #     if char in magazine:
    #         magazine.remove(char)
    #     else:
    #         return False
    # return True

    # Method 2: O(n+m)
    # magazine = Counter(magazine)
    # for char in ransomNote:
    #     if magazine[char] == 0:
    #         return False
    #     magazine[char] -= 1
    # return True