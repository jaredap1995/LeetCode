var solution = function(colors, neededTime){
    let start = 0
    let end = 1
    let sol = 0

    var arrSum = arr => arr.reduce((a,b) => a+b, 0)

    while (end < colors.length){
        if (colors[end] === colors[start]){
            let temp = end
            while (temp < colors.length){
                if (colors[temp] === colors[start]) {
                    temp ++
                } else 
                { 
                    break 
                }
            }
            let group = neededTime.slice(start, temp)
            let groupTime = arrSum(group) - Math.max(...group)
            sol += groupTime
            start = temp
            end = start + 1
        } else {
            start ++
            end ++
        }
    }

    return sol
}