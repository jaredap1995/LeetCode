var solution = function(s){
    let maxScore = 0
    let zerosLeft = 0;
    let onesRight = s.match(/1/g)
    if (onesRight === null){
        return s.length -1
    } else {
        onesRight = onesRight.length
    }

    for (let i = 0; i< s.length-1; i++){
        s[i] === '1' ? onesRight -- : onesRight
        s[i] === '0' ? zerosLeft ++ : zerosLeft
        maxScore = Math.max(maxScore, zerosLeft + onesRight)
    }

    return maxScore
}