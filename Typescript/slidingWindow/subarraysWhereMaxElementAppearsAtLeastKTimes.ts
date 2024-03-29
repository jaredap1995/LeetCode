var solution2 = function(nums: number[], k: number): number{
    let m: number = Math.max(...nums)
    let n: number = nums.length
    let right: number = 0
    let left: number = 0
    let res: number = 0

    while (right < n){
        if (nums[right] === m) k--
        right ++
        while (k === 0){
            if (nums[left] === m) k ++
            left ++
        }

        res += left
    }

    return res

}
