"""
You are given an array prices where prices[i] is 
the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to 
buy one stock and choosing a different day in the future to 
sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

"""

class Solution(object):
    def maxProfit(self, prices):
        start=0
        end=1
        max_profit=0
        while end < len(prices):
            profit=prices[end]-prices[start]
            if prices[start] < prices[end]:
                max_profit=(max(profit, max_profit))
            else:
                start=end
            end+=1
        return max_profit
