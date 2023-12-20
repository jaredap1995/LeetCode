prices = [98,54,6,34,66,63,52,39]
money = 62

class Solution:
    def buyChoco(self, prices, money: int) -> int:
        prices.sort()
        return money if money < (prices[0] + prices[1]) else (money - (prices[0]+prices[1]))
print(Solution().buyChoco(prices, money))