class Solution(object):
    def coinChange(coins, amount):
        if amount == 0: return 0
        coins.sort()

        min_count = [float('inf')]*(amount+1)
        min_count[0]=0

        for i in range(1,amount+1):
            for coin in coins:
                if coin>i:
                    break
                min_count[i]=min(min_count[i], 1+min_count[i-coin])

        if min_count[amount] == float('inf'):
            return -1
        else:
            return min_count[amount]
        