/**
 * @param {number []}
 * @return {number [][]}
 */

var subsets2 = function (nums) {
    let result = []
    nums.sort(function(a,b) {return a-b}) //Sorts array in ascending order by substracting a-b and using values to decide order

    var backtrack = (index, current) => {
        result.push([...current])
        for (let i = index; i<nums.length; i++){
            if (i > index && nums[i]==nums[i-1]) continue
            current.push(nums[i])
            backtrack(i+1, current)
            current.pop()
        }
    }
    backtrack(0,[])
    return result
}