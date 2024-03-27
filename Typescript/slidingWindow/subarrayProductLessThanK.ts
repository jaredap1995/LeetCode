var solutio = function(nums: number[], k: number): number {
    if (k <= 1) return 0
    let prod: number = 1
    let left: number = 0
    let count: number = 0

    for (let right = 0; right < nums.length; right++){
        prod *= nums[right]

        while (prod >= k) {
            prod = Math.floor(prod/nums[left])
            left ++
        }

        count += right - left + 1
    }

    return count
}