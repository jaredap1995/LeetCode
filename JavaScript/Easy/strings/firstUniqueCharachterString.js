var solution = function(s){
    var Counter = (arr) => {
        let dict = new Map()
        for (let i = 0; i<s.length; i++){
            dict.set(arr[i], (dict.get(arr[i]) || 0) + 1)
        }

        return dict
    }

    let dict = Counter(s)

    let res = -1
    for (let i = 0; i<s.length; i++){
        if (dict.get(s[i]) === 1){
            res= i
            break
        }
    }

    return res
}