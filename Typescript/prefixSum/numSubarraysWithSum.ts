var solution = function(nums: number[], goal: number): number {
    let res = 0
    let pre: object = {0:1}
    let cumsum = 0;
    for (let i = 0; i< nums.length; i++){
        cumsum += nums[i]
        res += (pre[cumsum-goal] ?? 0)
        pre[cumsum] = (pre[cumsum] || 0) + 1
    }

    return res
}