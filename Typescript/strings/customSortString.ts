var solution = function (order: string, s: string): string {
    let res = ""
    let temp: [string, number][] = [] 
    for (let char of s){
        if (order.includes(char)){
            let idx = order.indexOf(char)
            temp.push([char, idx])
        }
    }

    temp.sort((a,b) => a[1] - b[1])
    for (let i = 0; i< temp.length; i++){
        res += temp[i][0]
    }

    console.log(res)    
    let idx = 0
    let length = s.length

    while (idx < length) {
        let val = s[idx]
        if (!order.includes(val)){
            res += val
        }
        idx ++
    }

    return res
};