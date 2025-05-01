# Given an array prices where prices[i] is the price of a given stock on the ith day,
# return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# You must buy before you sell and you cannot sell a stock before you buy it.
# Input: prices = [7,1,5,3,6,4]
# Output: 5

# def maxProfit(self, prices):
    # input: 1 list; output: num
    
    # Method 1: O(n^2)
    # loop through the list
        # loop through the rest of the list
            # profit = list[j] - list[i]
            # check if profit > max_profit:
                # max_profit = profit
    # return max_profit

    # Method 2: O(n)
    # set min_price to the first price
    # loop through the rest of the list
            # if price < min_price, then replace min_price
        # if price - min_price > max_profit, then replace max_profit
    # return max_profit