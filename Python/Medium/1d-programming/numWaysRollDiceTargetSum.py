def solution(n,k,target):
    mod = 10 ** 9 + 7
    # A DP array for every face of every die
    dp = [[-1] for _ in range(k+1) for _ in range(n+1)]

    def dfs(dp, n,k,target):
        # Base case, we have no dice left and the target is 0 (we have reached target) ==> return 1 way
        if target == 0 and n == 0:
            return 1
        
        # We have no die left to roll, but target is not 0, hence we return 0
        if n == 0 or target <= 1:
            return 0
        
        # memoization check
        if dp[n][target] != -1:
            return dp[n][target] % mod

        # Iterate to find number of ways
        ways = 0
        # For every value, we check what the potential results could be with one less die and for each value
        for i in range(1, k+1):
            ways = (ways + dfs(dp, n-1, k, target-i)) % mod

        # Store value
        dp[n][target] = ways % mod
        return dp[n][target]
    
    return dfs(dp, n, k, target)
