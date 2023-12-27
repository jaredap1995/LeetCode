var solution = function(n,k,target){
    let mod = 10 **9 + 7
    let dp = new Array(n+1).fill(0).map(() => new Array(target+1).fill(-1))

    var dfs = (dp, n, k, target) => {
        if (target === 0 && n === 0) return 1
        if (target <= 0 || n === 0) return 0

        if (dp[n][target] !== -1) return dp[n][target] % mod

        let ways = 0
        for (let i = 1; i< k+1; i++){
            ways = (ways + dfs(dp, n-1, k, target-i))
        }

        dp[n][target] = ways % mod
        return dp[n][target]

    }

    return dfs(dp, n, k, target)
}