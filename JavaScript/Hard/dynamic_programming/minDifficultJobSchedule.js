var solution = function(jobDifficulty, d){
    if (jobDifficulty.length < d) return -1

    let jd = jobDifficulty.length
    let dp = new Array(jd+1).fill(0).map(() => new Array(d+1).fill(0))

    for (let i = 0; i< d+1; i++){
        dp[jd][i] = 10**6
    }

    for (let i = 0; i< jd; i++){
        dp[i][1] = Math.max(...jobDifficulty.slice(i))
    }

    for (let i = jd; i>-1; i--){
        for (let j = 2; j< d+1; j++){
            let ans = 10**6
            let mx = -1
            for (let k = i; k<jd; k++){
                mx = Math.max(mx, jobDifficulty[k])
                temp = mx + dp[k+1][j-1]
                ans = Math.min(temp, ans)
            }
            dp[i][j] = ans
        }
    }

    return dp[0][d]
}