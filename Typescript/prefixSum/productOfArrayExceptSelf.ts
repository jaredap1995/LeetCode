var solution2 = function(nums: number[]): number[] {
    let res: number [] = new Array(nums.length).fill(1)
    let pre = 1

    for (let i = 0; i< nums.length; i++){
        res[i] *= pre
        pre *= nums[i]
    }

    let post = 1
    for (let i = nums.length-1; i > -1; i--){
        res[i]*= post
        post *= nums[i]
    }

    return res
}