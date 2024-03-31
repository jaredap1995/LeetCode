var sol = function(nums: number[], minK: number, maxK: number): number {
    let minl: number = -1
    let maxl: number = -1
    let res = 0
    let left: number = 0

    for (let right = 0; right < nums.length; right ++){
        let val = nums[right]
        if (val < minK || val > maxK){
            left = right + 1
            minl = -1
            maxl  -1
        } else {
            if (right === minK) minl = right
            if (right === maxK) maxl = right
            res += Math.max(0, Math.min(minl, maxl) - left + 1)
        }
    }
    return res
}