var solution = function(nums: number[]): number[] {
    let res = []
    for (let x of nums){
        x = Math.abs(x)
        if (nums[x-1] < 0) res.push(x)
        nums[x-1] = nums[x-1] * -1
    }

    return res
}