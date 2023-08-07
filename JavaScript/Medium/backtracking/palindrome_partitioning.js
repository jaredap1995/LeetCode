/**
 * @param {string} s
 * @return {string [][]}
 */

var partition = function (s) {
    var reverseString = (s) => {
        var splitString = string.split("");
        var reverse = splitString.reverse();
        var join = reverse.join("")

        return join
    }

    let result = []
    var backtrack = (start, s, current) => {
        if (start >= s.length){
            result.push([...current])
            return
        }
        for (let j = start; j <s.length; j++){
            if (s.slice(start, j+1)=="".concat(reverseString(s.slice(start,j+1)))){
                current.push(s.slice(start, j+1))
                backtrack(j+1, s, current)
                current.pop()
            }
        }
    }
    backtrack(0,s,[])
    return result
}