var solution = function(nums: number[], k: number): number {
    let res: number = 0
    let left: number = 0
    let n: number = nums.length
    let hashmap: object = {}

    for (let right = 0; right < n; right ++){
        hashmap[nums[right]] = (hashmap[nums[right]] | 0) + 1
        if (hashmap[nums[right]] > k){
            while (nums[right] !== nums[left]){
                hashmap[nums[left]] --
                left ++
            }
            hashmap[nums[left]] --
            left ++
        }
        res = Math.max(res, (right - left + 1))
    }

    return res
}