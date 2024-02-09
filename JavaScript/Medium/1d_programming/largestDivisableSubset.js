var solution = (nums) => {
    let subsets = new Map()
    subsets.set(-1, new Set())

    nums.sort((a,b) => a-b)

    for (const num of nums){
        let divisors = []
        for (const [key, value] of subsets){
            if (num % key === 0){
                divisors.push(value)
            }
        }

        let maxSize = 0
        let maxSubset = new Set()
        for (let subset of divisors){
            if (subset.size > maxSize) {
                maxSize = subset.size
                maxSubset = new Set(subset)
            }
        }

        maxSubset.add(num)
        subsets.set(num, maxSubset)
    }

    let res = []
    let length = 0
    for (let arr of subsets.values()){
        if (arr.size > length) {
            length = arr.size
            res = Array.from(arr)
        }
    }

    return res
}