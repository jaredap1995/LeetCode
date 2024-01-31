var solution = function(temperatures){
    let n = temperatures.length
    let stack = []
    let answer = new Array(n).fill(0)
    for (let i = 0; i< n; i++){
        while (stack && temperatures[i] > temperatures[stack[stack.length-1]]){
            let cur = stack.pop()
            answer[cur] = i - cur
        }
        stack.push(i)
    }

    return answer
}