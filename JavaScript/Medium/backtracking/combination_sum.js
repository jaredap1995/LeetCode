/**
 * @param {number []} candidates
 * @param {number} target
 * @return {number [][]} 
 */

var combinationSum = (candidates, target) =>{
    let result = []
    var backtrack = (start, current_sum, current) => {
        if (current_sum > target){
            return
        }
        if (current_sum === target){
            result.push([...current])
            return
        }
        for (let i = 0; start<candidates.length; i++){
            current.push(candidates[i])

            backtrack(i, current_sum+candidates[i], current)

            current.pop()
        }
    }
    backtrack(0,0,[])
    return result
}