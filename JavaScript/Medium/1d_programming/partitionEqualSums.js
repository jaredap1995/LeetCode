var equalSums = (nums) => {
    let sum = 0
    nums.forEach(element => {
        sum+=element    
    });

    if (sum%2 != 0) {
        return false
    }

    let target = Math.floor(sum/2)
    let dp = new Array(target+1).fill(false)
    dp[0]=true

    for (let num of nums) {
        for (let i = target; i > num -1; i--){
            if (dp[i-num] == true){
                dp[i]=true
            }
        }
    }
    console.log(dp)
    return dp[target]
}



test=[1,5,11,5]
console.log(equalSums(test))