var rob = function(nums) {
    if (nums.length == 1) { return nums[0]}
    if (nums.length == 2) { return Math.max(nums[0], nums[1])}

    n=nums.length
    let robbed_1 = new Array(n-1).fill(0)
    let robbed_2 = new Array(n-1).fill(0)

    robbed_1[0]=nums[0]
    robbed_1[1]=Math.max(nums[0],nums[1])
    robbed_2[0]=nums[1]
    robbed_2[1]=Math.max(nums[1],nums[2])

    for (let i = 2; i<nums.length; i++) {
        robbed_1[i] =Math.max(robbed_1[i-2]+nums[i], robbed_1[i-1])   
        robbed_2[i]=Math.max(robbed_2[i-2]+nums[i+1], robbed_2[i-1])
    }

    return Math.max(robbed_1[n-2], robbed_2[n-2])
}