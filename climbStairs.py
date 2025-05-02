# Questions: You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Input: n = 2
# Output: 2
# Input: n = 3
# Output: 3

# def climbStairs(self, n):

    # Method 1: O(2^n), O(n)
    # recursion to find the number of ways by going through the tree from n to 0
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # Method 2: O(n), O(n) ButtomUp DP with dp list
    # set up dp array to store number of ways
    # loop through and fill the dp list
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2

    # dp = [0] * (n + 1)
    # dp[1], dp[2] = 1, 2

    # for i in range(3, len(dp)):
    #     dp[i] = dp[i - 1] + dp[i - 2]
    
    # return dp[-1]

    # Method 3: O(n), O(1) ButtomUp DP with two variables
    # set up two variables to store the number of ways
    # prev, curr = 1, 2
    # for i in range(3, n+1):
    #     prev, curr = curr, prev + curr
    # return curr