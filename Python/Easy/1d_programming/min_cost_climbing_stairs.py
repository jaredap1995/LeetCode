class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        n=len(cost)
        dp = [0]*(n+1)
        dp[n]=0
        print(dp)

        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i]+min(dp[i+1], dp[i+2])
            print(dp[i])
            print(i)

        return min(dp[0], dp[1])
    

cost = [10, 15, 20]
print(Solution().minCostClimbingStairs(cost))