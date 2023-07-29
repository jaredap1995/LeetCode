/**
 * @param {number []} nums
 * @return {number [][]}
 */

Set()

var permute = function (nums) {
    let result = []
    let visited = new Set()

    var backtrack = (result, visited, subset, nums) => {
        if (subset.length === nums.length){
            result.push([...subset])
        }

        for (let i = 0; i<nums.length; i++) {
            if (!visited.has(i)) {
                visited.add(i)
                backtrack(result, visited, subset, nums)
                visited.remove(i)
            }
        }
    }

    

}