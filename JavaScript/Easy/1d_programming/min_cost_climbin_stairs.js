var minCostClimbingStairs = function(cost) {
    let n = cost.length //top
    if (n==1) {return cost[0]}
    if (n==2) {return Math.min(cost[0], cost[1])}

    let dp = new Array(n).fill(0)
    dp[n] = 0


    for (let step = n-1; step >= 0; step--) {
        if(step == n-1) { dp[step] = cost[step]}
        else {dp[step] = cost[step] + Math.min(dp[step+1], dp[step+2])}
    }

    console.log(dp)
    return Math.min(dp[0], dp[1])
};


cost = [10,15,20]
console.log(minCostClimbingStairs(cost)) //15