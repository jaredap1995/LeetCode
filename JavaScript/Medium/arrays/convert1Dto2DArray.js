var solution = function(nums){
    let temp = new Set(nums)
    if (temp.size == nums.length){
        return [nums]
    }

    let counter = {}
    for (let i = 0; i< nums.length; i++){
        if (!counter[nums[i]]) { 
            counter[nums[i]] = 1
        } else {
            counter[nums[i]] ++
        }
    }

    let max_val = Math.max(...Object.values(counter))
    let res = new Array(max_val).fill(0).map(() => new Array())

    let i = 0
    while (i < max_val){
        for (const [k,v] of Object.entries(counter)){
            if (counter[k] === 0) continue
            res[v-1].push(k)
            counter[k] -- 
        }
        i ++
    }

    return res
}