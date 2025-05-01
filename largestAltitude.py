# Question: Given an integer array gain, where gain[i] is the net gain at the ith point, return the highest altitude of a person who can achieve after following the given rules.
# The altitude starts at 0 and each step in the gain array contributes to the altitude.

# Input: gain = [-5,1,5,0,-7]
# Output: 1

# def largestAltitude(self, gain):
    # input: list; output: num

    # Method 1: O(n^2)
    # loop through the list and add up the num in front of it
    # if it is larger than max, replace max and update the altitude
    # max_altitude = 0

    # for i in range(len(gain)):
    #     altitude = 0
    #     for j in range(0,i+1):
    #         altitude += gain[j]
    #     if altitude > max_altitude:
    #         max_altitude = altitude

    # return max_altitude
    
    # Method 2: O(n)
    # loop through the list and add them up one by one
    # store them into a list and see which value is the highest

    # total = 0
    # altitudes = [0]

    # for i in range(len(gain)):
    #     total += gain[i]
    #     altitudes.append(total)
    
    # return max(altitudes)

    