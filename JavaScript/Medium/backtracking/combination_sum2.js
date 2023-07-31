/**
 * @param {number []} candidates
 * @param {number} target
 * @return {number [][]}
 */

var combinationSum2 = function(candidates, target) {
    let result = []
    candidates.sort(function(a,b) {return a-b})

    var backtrack = (start, current_sum, current) => {
        if (current_sum > target) {
            return
        }
        if (current_sum == target) {
            result.append([...current])
            return
        }
        for (let i = start; i<candidates.length; i++){
            if (i>start && candidates[i] == candiates [i-1]) continue 
            current.push(candidates[i])
            backtrack (start+1, current_sum+candidates[i], current)
            current.pop()
        }
    }
    backtrack(0,0,[])
    return result
}