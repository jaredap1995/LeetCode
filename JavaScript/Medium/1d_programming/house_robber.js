var rob = function (nums) {
    if (nums.length === 1) { return nums[0]}
    if (nums.length === 2) { return Math.max(nums[0], nums[1])}

    let robbed = new Array(nums.length).fill(0)
    robbed[0]=nums[0]
    robbed[1]=Math.max(nums[0], nums[1])

    for (let i = 0; i<nums.length; i ++) {
        robbed[i]=Math.max(robbed[i-2]+nums[i], robbed[i-1])
    }

    return robbed[nums.length-1]
}