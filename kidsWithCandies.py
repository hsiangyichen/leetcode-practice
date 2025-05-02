# Question: Given the array candies and the integer extraCandies, where 
# candies[i] represents the number of candies the ith kid has, and
# extraCandies is the number of extra candies that you have, return a 
# boolean array result of length n where result[i] is true if after giving 
# the ith kid all the extra candies they will have the greatest number of 
# candies among all the kids or false otherwise.

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]

# def kidsWithCandies(self, candies, extraCandies):
    # input: list; output: list

    # Method 1: O(n^2)
    # result = []
    # for i in range(len(candies)):  
    #     isGreatest = True    
    #     for j in range(len(candies)):
    #         if candies[i] + extraCandies < candies[j]:
    #             isGreatest = False
    #             break
    #     result.append(isGreatest)
    # return result

    # Method 2: O(n)
    # max_candy = max(candies)
    # result = []

    # for candy in candies:
    #     if candy + extraCandies >= max_candy:
    #         result.append(True)
    #     else:
    #         result.append(False)
    # return result
    