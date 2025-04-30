class Solution(object):
    def maxProfit(self, prices):
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