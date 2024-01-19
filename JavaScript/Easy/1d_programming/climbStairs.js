var solution = (n)=>{
    if (n===1)return 1
    if (n===2) return 2
    let dp = new Array(n+1).fill(0)
    dp[1] = 1
    dp[2] = 2

    for (let i = 2; i<n+1; i++){
        if (dp[i]===0){
            dp[i] = dp[i-2]+dp[i-1]
        }
    }

    return dp[n]
}