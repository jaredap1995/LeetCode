var solution = function(low, high){
    let allDigits = '123456789'
    let res = []

    for (let windowSize = low.toString().length; windowSize < high.toString().length + 1; windowSize++){

        for (let start = 0; start<10-windowSize; start++){
            end = start+windowSize
            let curDigit = parseInt(allDigits.slice(start, end))
            if (curDigit >= low && curDigit <= high) res.push(curDigit)
        }
    }

    return res
}