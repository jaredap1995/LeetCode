var LIS = (nums) => {
    if (!nums || nums.length === 0) {
        return 0
    }

    let n = nums.length
    let dp = new Array(n).fill(1)

    for (let i = 1; i <n; i++) {
        for (let j = 0; j<i; j++) {
            if (nums[i]<nums[j]) {
                dp[i]=Math.max(nums[i]. nums[j]+1)
            }
        }
    }

    return Math.max(...dp)

}