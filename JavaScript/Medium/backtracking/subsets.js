/**
 * 
 * @param {number[]} nums
 * @return {number[][]}
 */

nums = [1,2,3]

var subsets = (nums) => {
    var answer = []
    for (let i = 0; i<nums.length; i++){
        var sublist = []
        for (let j = 0; j<nums.length; j++){
            if (i&&(1<j)) {
                sublist.push(nums[j])
            }
        }
        answer.push(sublist)
    }
    return answer
}

var subsets_2 = function(nums){
    var answer = []
    backtrack ([], 0)

    function backtrack(current, index){
        answer.push(current)
        for (let i = 0; i<nums.length; i++){
            backtrack(current.concat(nums[i]), i+1)
        }
    }
return answer
}

var subsets_3 = function (nums) {
    var result = [[]]
    for (let i = 0; i<nums.length; i++){
        let current = nums[i]
        let newSubSet = answer.map(subSet => [...subSet, current])
        result = result.concat(newSubSet)
    }
    return result
}